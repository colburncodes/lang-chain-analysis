import pandas as pd
import pandas_datareader.data as web
import sqlite3
from datetime import datetime

class DataLoader:
    def __init__(self, db_name="financial_data.db"):
        self.db_name = db_name
        self.economic_indicators_tickers = ['UNRATE', 'PAYEMS', 'ICSA', 'CIVPART', 'INDPRO']
        self.yield_curve_tickers = ['DGS1MO', 'DGS3MO', 'DGS6MO', 'DGS1', 'DGS2', 'DGS3', 'DGS5', 'DGS7', 'DGS10', 'DGS20', 'DGS30']
        self.production_data_tickers = ['SAUNGDPMOMBD', 'ARENGDPMOMBD', 'IRNNGDPMOMBD', 'SAUNXGO','DPCCRV1Q225SBEA',
                                        'QATNGDPMOMBD', 'KAZNGDPMOMBD', 'IRQNXGO', 'IRNNXGO', 'KWTNGDPMOMBD', 'IPN213111S', 'PCU213111213111']
    
    def clean_data(self, data):
        # Function to clean data, remove leading/trailing single quotes, and convert to numeric
        cleaned_data = data.applymap(lambda x: x.strip("'") if isinstance(x, str) else x)
        cleaned_data = cleaned_data.apply(pd.to_numeric, errors='coerce')
        return cleaned_data
    
    def fetch_and_insert_data(self, tickers, table_name):
        start_date = '2000-12-31'
        end_date = datetime.now().strftime('%Y-%m-%d')
        try:
            data = web.DataReader(tickers, 'fred', start_date, end_date)
            data = data.interpolate(method='quadratic').bfill().ffill()
            data = data.resample('D').ffill().bfill()

            # Clean the data to handle formatting issues
            data = self.clean_data(data)

            # Convert the index (which is the date) to the correct format
            data.index = pd.to_datetime(data.index).strftime('%Y-%m-%d %H:%M:%S')

            with sqlite3.connect(self.db_name) as conn:
                data.to_sql(table_name, conn, if_exists='replace', index_label='Date')
            print(f"Data inserted into {table_name} table")
        except Exception as e:
            print(f"Failed to fetch and insert the data: {e}")

def main():
    db_name = "financial_data.db"
    loader = DataLoader(db_name)
    loader.fetch_and_insert_data(loader.economic_indicators_tickers, 'economic_indicators')
    loader.fetch_and_insert_data(loader.yield_curve_tickers, 'yield_curve_prices')
    loader.fetch_and_insert_data(loader.production_data_tickers, 'production_data')

if __name__ == "__main__":
    main()
