import requests
from urllib.parse import urljoin

def submit_form(form_details, url, value):
    """
    Submits a form with the given payload (value) and returns the response.
    """
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}

    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            data[input["name"]] = value
        else:
            data[input["name"]] = input.get("value", "")

    try:
        if form_details["method"] == "post":
            return requests.post(target_url, data=data, timeout=10)
        return requests.get(target_url, params=data, timeout=10)
    except Exception as e:
        print(f"Request failed: {e}")
        return None
