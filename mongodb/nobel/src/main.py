from loguru import logger
import requests
from pymongo import MongoClient
from src.utils import get_json_from_url, insert_data_into_collection

def nobel_data_crawler():
    # URLs
    data_url = "https://assets.datacamp.com/production/repositories/1838/datasets/"
    laureates_url = data_url + "f402fa7be837b9cd4890f4e1c59a7377693ba36c/laureates.json"
    prizes_url = data_url + "3fde64719bc3226b593a1c261f715566ea6284b2/prizes.json"

    # MongoDB client
    client = MongoClient()
    db = client["nobel"]

    try:
        # Laureates
        laureates_data = get_json_from_url(laureates_url)
        laureates_count = insert_data_into_collection(db, "laureates", laureates_data)
        logger.info(f"{laureates_count} documents stored in laureates collection")

        # Prizes
        prizes_data = get_json_from_url(prizes_url)
        prizes_count = insert_data_into_collection(db, "prizes", prizes_data)
        logger.info(f"{prizes_count} documents stored in prizes collection")

    except requests.exceptions.RequestException as e:
        logger.error(f"Error during data retrieval: {e}")

if __name__ == "__main__":
    nobel_data_crawler()
