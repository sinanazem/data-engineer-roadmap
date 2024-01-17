import requests
import json

def get_metal_data():
    url = f"{}"
    response = requests.get(url)
    if response.ok:
        data = response.json()
    return data