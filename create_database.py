import sqlite3

def create_tables(db_name):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()

        # Create economic indicators table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS economic_indicators (
            Date TEXT PRIMARY KEY,
            UNRATE REAL,
            PAYEMS REAL,
            ICSA REAL,
            CIVPART REAL,
            INDPRO REAL         
        )''')
        print("Tables created successfully")

create_tables("financial_data.db")