import sqlite3

def create_tables(db_name):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()

        # economic indicators table if it doesn't exist
        # FRED series IDs for unemploymnet rate, non-farm payrolls, initial jobless claims, civilian participation rate, and industrial production
        cursor.execute('''CREATE TABLE IF NOT EXISTS economic_indicators (
            Date TEXT PRIMARY KEY,
            UNRATE REAL,
            PAYEMS REAL,
            ICSA REAL,
            CIVPART REAL,
            INDPRO REAL         
        )''')

        # yield curve prices table if it doesn't exist
        # fred/series/observations
        cursor.execute('''CREATE TABLE IF NOT EXISTS yield_curve_prices (
            Date TEXT PRIMARY KEY,
            DGS1MO REAL,
            DGS3MO REAL,
            DGS6MO REAL,
            DGS1YR REAL,  
            DGS2YR REAL,
            DGS3YR REAL,
            DGS5YR REAL,
            DGS7YR REAL,
            DGS10YR REAL,
            DGS20YR REAL,
            DGS30YR REAL
            )''')
        
        # production data table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS production_data (
            Date TEXT PRIMARY KEY,
            Saudi_GDP_Monthly_BD REAL,  -- Assuming 'BD' is a relevant unit or identifier
            UAE_GDP_Monthly_BD REAL,
            Iran_GDP_Monthly_BD REAL,
            Saudi_Exports_Oil REAL,
            Qatar_GDP_Monthly_BD REAL,
            Kazakhstan_GDP_Monthly_BD REAL,
            Iraq_Exports_Oil REAL,
            Iran_Exports_Oil REAL,
            Kuwait_GDP_Monthly_BD REAL,
            Industrial_Production_Index REAL,  -- Assuming 'IPN213111S' is an index code
            Price_Change_Utility REAL,  -- Assuming 'PCU213111213111' relates to price change
            GDP_Commercial_Vehicle REAL  -- Assuming 'DPCCRV1Q225SBEA' relates 
            )''')
        
        # business_cycles table with an auto-increment ID as the primary key
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS business_cycles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Peak_Month TEXT,
                Trough_Month TEXT,
                Start_Date TEXT,
                End_Date TEXT,
                Phase TEXT
            )
        ''')

        # Optionally, add indexes on date columns if they will be used in joins or queries often
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_econ_date ON economic_indicators (Date)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_yield_date ON yield_curve_prices (Date)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_prod_date ON production_data (Date)')
        
        print("Tables created successfully")
if __name__ == "__main__":
    create_tables("financial_data.db")
