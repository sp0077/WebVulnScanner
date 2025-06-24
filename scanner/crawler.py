# crawler.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_forms(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    details = {}
    action = form.attrs.get("action", "").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details
