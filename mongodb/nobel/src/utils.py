import requests


def get_json_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def insert_data_into_collection(db, collection_name, data):
    collection = db[collection_name]
    collection.insert_many(data)