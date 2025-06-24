
🛡️ Web Vulnerability Scanner

A lightweight web vulnerability scanner built using **Python** and **Flask**. This tool automatically detects common vulnerabilities in web applications such as **SQL Injection (SQLi)** and **Cross-site Scripting (XSS)** through form analysis and payload testing.

---

# 🚀 Features

- 🔍 Crawls target web pages and identifies form inputs
- 💉 Injects SQLi and XSS payloads into parameters
- 📄 Logs and reports vulnerabilities found
- 🌐 Simple web interface with Bootstrap styling
- 📂 Organized modular code structure for easy extension

---

# 📁 Project Structure

WebVulnScanner/
├── app.py
├── requirements.txt
├── scanner/
│   ├── crawler.py
│   ├── detector.py
│   ├── logger.py
│   ├── payloads.py
│   └── submitter.py
├── scanner/payloads/
│   ├── sqli.txt
│   └── xss.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── reports/
└── scan\_log.txt

---

# ⚙️ Installation

1. Clone the repository:
   git clone https://github.com/your-username/WebVulnScanner.git
   cd WebVulnScanner

2. Install dependencies:
   pip install -r requirements.txt
  

3. Run the application:
   python app.py


---


# 🧪 Usage

1. Launch the scanner via the Flask UI.
2. Enter the target URL in the scan box.
3. Click **"Scan"** to initiate vulnerability detection.
4. Check the report saved at `reports/scan_log.txt`.

---

# 🛠️ Technologies Used

* Python 3.10
* Flask (Web framework)
* Requests (HTTP requests)
* HTML/CSS + Bootstrap (Frontend)

---

# 📝 Report Output Example


[VULNERABLE] SQL Injection detected on http://example.com/login
Payload: ' OR '1'='1

[VULNERABLE] XSS vulnerability found in http://example.com/search
Payload: <script>alert('XSS')</script>

---

# 📌 Future Enhancements

* Add CSRF, SSRF, and file inclusion detection
* Export reports in CSV and PDF formats
* Scan history and dashboard with analytics
* Docker container support

---

# 👤 Author

**Sarvesh Pandekar**
Computer Science  | 2025
GitHub: [@sp0077](https://github.com/sp0077)

---

# 📄 License
This project is open-source and available under the [MIT License](LICENSE).
