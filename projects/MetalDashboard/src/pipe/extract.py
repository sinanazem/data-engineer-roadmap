import requests
import json

def make_gapi_request():
    api_key = "goldapi-4a1o6rlrk555jk-io"
    symbol = "XAU"
    curr = "USD"
    date = ""

    url = f"https://www.goldapi.io/api/{symbol}/{curr}{date}"
    
    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        result = response.text
        print(result)
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))

make_gapi_request()


# def get_metal_data():
#     url = f"{}"
#     response = requests.get(url)
#     if response.ok:
#         data = response.json()
#     return data