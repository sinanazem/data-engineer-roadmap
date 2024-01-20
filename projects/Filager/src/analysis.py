import pathlib
import pandas as pd
import jdatetime
from loguru import logger
import re

logger.add("analysis.log", level="INFO", format="{time} {level} {message}", rotation="1 day", retention="7 days")

def extract_date_from_file_path(file_path):
    pattern = r'(\d{4}-\d{2}-\d{2})'
    match = re.search(pattern, file_path)
    if match:
        extracted_date = match.group(1)
        return extracted_date
    else:
        return None


class StockAnalysis:
    
    def __init__(self, datalake_path):
        
        self.datalake_path = datalake_path
        self.data = self.data_preparation()
    
    
    def data_preparation(self):
        datalake_path = pathlib.Path(self.datalake_path)
        csv_files = datalake_path.glob('*.csv')
        dfs = []

        for csv_file in csv_files:
            df = pd.read_csv(csv_file)
            
            
            logger.info(f" Data read from {csv_file} successfully!")
            logger.info(f" Shape of Data:  {df.shape} successfully!")
            # logger.info(f" Sample of Data:  {df.sample(3)} successfully!")
            
            date = extract_date_from_file_path(str(csv_file))
            df["تاریخ شمسی"] = date
            df["تاریخ میلادی"] = jdatetime.date.togregorian(jdatetime.datetime.strptime(date, format="%Y-%m-%d"))      
            
            dfs.append(df)
            
        concatenated_df = pd.concat(dfs, ignore_index=True)
        concatenated_df["تاریخ میلادی"] = pd.to_datetime(concatenated_df["تاریخ میلادی"])

        return concatenated_df
    
    
    def get_top_volume_stock_symbols(self, number=10):
        return self.data.groupby("نماد")["حجم"].sum().sort_values(ascending=False)[:number]
    
    def get_top_value_stock_symbols(self, number=10):
        return self.data.groupby("نماد")["ارزش"].sum().sort_values(ascending=False)[:number]
    
    def get_statistical_analysis_by_symbol(self, symbol):
        df = self.data
        df = df[df['نماد'] == symbol].describe()
        
        return self.data
    
if __name__ == "__main__":
    obj = StockAnalysis("/mnt/c/Users/user/OneDrive/Desktop/data-engineer-roadmap/projects/Filager/src/datalake")
    print(obj.get_top_volume_stock_symbols())
    print(obj.get_top_volume_stock_symbols())
    print(obj.get_statistical_analysis_by_symbol("دي"))
    
    
    
    
    
    

        
    