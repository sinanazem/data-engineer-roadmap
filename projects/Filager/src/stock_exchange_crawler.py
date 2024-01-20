import requests
import pathlib
import pandas as pd
import jdatetime
from tqdm import tqdm
from loguru import logger

logger.add("stock_exchange_crawler.log", level="INFO", format="{time} {level} {message}", rotation="1 day", retention="7 days")

def url_genrator(jalali_date):
    excel_url = f"http://members.tsetmc.com/tsev2/excel/MarketWatchPlus.aspx?d={jalali_date}"
    return excel_url


def url_downloader(excel_url, save_path):
    try:
        response = requests.get(excel_url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            logger.info(f"Download successful. File saved at: {save_path}")
        else:
            logger.info(f"Failed to download. Status code: {response.status_code}")
    except Exception as e:
        logger.error("We have error in url_downloader Error: {e}")
        


def download_tehran_stock_exchange_files(start_date, end_date):
    
    #create folder
    data_dir = pathlib.Path(f'./stage')
    data_dir.mkdir(parents=True, exist_ok=True)
    try :
        start_date = jdatetime.datetime.strptime(start_date, format="%Y-%m-%d").date()
        end_date = jdatetime.datetime.strptime(end_date, format="%Y-%m-%d").date()
        
        interval = (end_date - start_date).days
        for i in tqdm(range(0,interval+1)):
            jalali_date = start_date + jdatetime.timedelta(days=i)
            
            # Skip Weekends
            if jalali_date.weekday() not in (5,6):
                url = url_genrator(jalali_date=jalali_date.__str__())
                url_downloader(excel_url=url, save_path=f"./stage/tehran_stock_exchange_{jalali_date.__str__()}.xlsx")
            
    except Exception as e:
        logger.error(f"we have error: {e}")

if __name__ == "__main__":
    
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--startdate',help='Start Date Tehran Exchange Market')
    parser.add_argument('-e','--enddate',help='End Date Tehran Exchange Market')
    args = parser.parse_args()


    download_tehran_stock_exchange_files(args.startdate, args.enddate)
