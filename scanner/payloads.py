import os

# Adjust if your payloads are elsewhere
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
PAYLOAD_DIR = os.path.join(BASE_PATH, "payloads")

def load_payloads(type):
    """
    Load payloads from scanner/payloads/ directory.
    :param type: 'xss' or 'sqli'
    :return: list of payload strings
    """
    path = os.path.join(PAYLOAD_DIR, f"{type}.txt")
    if not os.path.exists(path):
        return []
    
    with open(path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]
