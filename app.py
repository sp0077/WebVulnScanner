from flask import Flask, render_template, request, send_file
from scanner.crawler import get_all_forms, get_form_details
from scanner.submitter import submit_form
from scanner.detector import is_vulnerable
from scanner.payloads import load_payloads
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import requests
import io
from urllib.parse import urljoin

app = Flask(__name__)
last_results = []

@app.route("/", methods=["GET", "POST"])
def index():
    global last_results
    results = []

    if request.method == "POST":
        target_url = request.form.get("url")

        if not target_url.startswith("http"):
            target_url = "http://" + target_url

        forms = get_all_forms(target_url)
        xss_payloads = load_payloads("xss")
        sqli_payloads = load_payloads("sqli")

        for form in forms:
            form_details = get_form_details(form)

            # Check for XSS
            for payload in xss_payloads:
                response = submit_form(form_details, target_url, payload)
                if response:
                    vuln_type = is_vulnerable(response, payload, expected="XSS")  # for xss payloads
                    if vuln_type:
                        results.append({
                            "vuln_type": vuln_type,
                            "payload": payload,
                            "url": target_url
                        })


            # Check for SQLi
            for payload in sqli_payloads:
                response = submit_form(form_details, target_url, payload)
                if response:
                    vuln_type = is_vulnerable(response, payload, expected="SQLi")
                    if vuln_type:
                        results.append({
                            "vuln_type": vuln_type,
                            "payload": payload,
                            "url": target_url
                        })


    last_results = results
    return render_template("index.html", results=results)

def generate_pdf(results):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, height - 50, "Web Vulnerability Scan Report")

    p.setFont("Helvetica", 12)
    y = height - 80
    if not results:
        p.drawString(50, y, "No vulnerabilities found.")
    else:
        for idx, result in enumerate(results, start=1):
            if y < 100:
                p.showPage()
                y = height - 50
            p.drawString(50, y, f"{idx}. [{result['vuln_type']}] Payload: {result['payload']}  URL: {result['url']}")
            y -= 20

    p.save()
    buffer.seek(0)
    return buffer

@app.route("/download-pdf")
def download_pdf():
    global last_results
    pdf_buffer = generate_pdf(last_results)
    return send_file(pdf_buffer, as_attachment=True, download_name="vulnerability_report.pdf", mimetype="application/pdf")

if __name__ == "__main__":
    app.run(debug=True)
