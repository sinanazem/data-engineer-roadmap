import requests
import pathlib
import pandas as pd
import jdatetime
from tqdm import tqdm
from loguru import logger

logger.add("transform.log", level="INFO", format="{time} {level} {message}", rotation="1 day", retention="7 days")

def change_format_to_csv(stage_path, datalake_path):
    
    try:
    
        df = pd.read_excel(stage_path, skiprows=2)
        
        if df.shape != 0:
            df.to_csv(datalake_path,encoding="utf-8", index=False)
            logger.info(f"format changed successfully!")
        else:
            logger.info(f"{stage_path} empty!")
    except Exception as e:
        logger.error(f" We have a error: {e}")

def change_format_store(stage_path, delete_excel=False):
    
    excel_file_path_list = pathlib.Path(stage_path).resolve()
    
    datalake_dir = excel_file_path_list.parent / 'datalake'
    datalake_dir.mkdir(parents=True, exist_ok=True)
    try:
        for excel_file_path in excel_file_path_list.glob('*'):
            print(excel_file_path)
            csv_file_path = datalake_dir /  (excel_file_path.stem + '.csv')

            change_format_to_csv(excel_file_path, csv_file_path)

            if delete_excel:

                # Check if the file exists before attempting to delete
                if excel_file_path.exists():
                    try:
                        # Delete the file
                        excel_file_path.unlink()
                        print(f"{excel_file_path} has been deleted successfully.")
                    except Exception as e:
                        print(f"Error deleting {excel_file_path}: {e}")
                else:
                    print(f"The file {excel_file_path} does not exist.")
    except Exception as e:
        logger.error(f" We have a error: {e}")


if __name__ == "__main__":
    
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--stagedir',help='Stage Directory file Path')
    parser.add_argument('-d','--delete',help='Delete Excel Files')
    args = parser.parse_args()
    
    change_format_store(args.stagedir, bool(args.delete))