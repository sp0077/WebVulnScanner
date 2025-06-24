import datetime

def log_vulnerability(url, payload, response_text):
    with open("reports/scan_log.txt", "a") as log:
        log.write(f"[{datetime.datetime.now()}] Vulnerable URL: {url}\n")
        log.write(f"Payload: {payload}\n")
        log.write(f"--- Snippet ---\n{response_text[:300]}\n\n")