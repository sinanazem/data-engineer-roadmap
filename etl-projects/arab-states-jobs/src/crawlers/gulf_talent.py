import requests
from bs4 import BeautifulSoup
import pandas as pd


URL = "https://www.gulftalent.com/jobs/search?pos_ref=Data&frmPositionCountry=#!?category=&industry=&seniority=&country=&city=&employment_type=&has_external_application=&keyword=Data"

def job_list_crawler():
    r = requests.get(URL)
    soup = BeautifulSoup(r.text)
    job_list_html = soup.find_all(class_='ga-job-impression ga-job-click job-results-item section')

    list_of_dict = []
    for job in job_list_html:
        position = job.find(class_='title').text.strip()
        date = job.find(class_='date').text.strip()
        company = job.find(class_="company-name").text.strip()
        location = job.find(class_="location").text.strip()
        detail_link = job['href']

        dict_ = { 
            "position" : position,
            "date" : date,
            "company" : company,
            "location" :location,
            "detail_link" : detail_link
            }
        list_of_dict.append(dict_)
        return list_of_dict

def store_to_csv(list_of_dict, file_path):
    df = pd.DataFrame(list_of_dict)
    df.to_csv(file_path)