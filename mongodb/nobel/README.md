# Nobel Prize Data Extraction and MongoDB Insertion

## Overview

The **Nobel Prize Data Extraction** project is a Python script that retrieves Nobel Prize data from the DataCamp API and stores it in a MongoDB database. This script utilizes the [loguru](https://github.com/Delgan/loguru) library for logging, [requests](https://docs.python-requests.org/en/latest/) for making HTTP requests, and [pymongo](https://pymongo.readthedocs.io/en/stable/) for interacting with MongoDB.

## Dependencies

- [loguru](https://github.com/Delgan/loguru)
- [requests](https://docs.python-requests.org/en/latest/)
- [pymongo](https://pymongo.readthedocs.io/en/stable/)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/sinanazem/data-engineer-roadmap.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the Nobel Prize Data Extraction script, execute the following command:

```bash
python main.py
```

## Configuration

The script does not require extensive configuration. However, you may customize the MongoDB connection details or the URLs for data retrieval. Open the script and modify the relevant variables:

```python
# MongoDB client
client = MongoClient()
db = client["nobel"]

# DataCamp API URLs
data_url = "https://assets.datacamp.com/production/repositories/1838/datasets/"
laureates_url = data_url + "f402fa7be837b9cd4890f4e1c59a7377693ba36c/laureates.json"
prizes_url = data_url + "3fde64719bc3226b593a1c261f715566ea6284b2/prizes.json"
```

## License

This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.

---

Feel free to tailor this README file to better suit your project's unique details and requirements.
