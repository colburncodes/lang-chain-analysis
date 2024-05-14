import sqlite3

def insert_business_cycle_data(db_name):
    business_cycles = [
        {"peak": "1999-03-01", "trough": "2001-03-01", "start": "1999-03-01 00:00:00", "end": "2001-03-01 00:00:00", "phase": "Expansion"},
        {"peak": "2001-03-01", "trough": "2001-11-01", "start": "2001-03-01 00:00:00", "end": "2001-11-01 00:00:00", "phase": "Contraction"},
        {"peak": "2001-11-01", "trough": "2007-12-01", "start": "2001-11-01 00:00:00", "end": "2007-12-01 00:00:00", "phase": "Expansion"},
        {"peak": "2007-12-01", "trough": "2009-06-01", "start": "2007-12-01 00:00:00", "end": "2009-06-01 00:00:00", "phase": "Contraction"},
        {"peak": "2020-02-01", "trough": "2020-04-01", "start": "2009-06-01 00:00:00", "end": "2020-02-01 00:00:00", "phase": "Expansion"},
        {"peak": "2020-02-01", "trough": "2020-04-01", "start": "2020-02-01 00:00:00", "end": "2020-04-01 00:00:00", "phase": "Contraction"},
        {"peak": "2021-12-01", "trough": "2022-03-31", "start": "2020-04-01 00:00:00", "end": "2022-03-11 00:00:00", "phase": "Expansion"}
    ]
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        
        for row in business_cycles:
            cursor.execute('''
                INSERT INTO business_cycles (Peak_Month, Trough_Month, Start_Date, End_Date, Phase)
                VALUES (?, ?, ?, ?, ?)
            ''', (row['peak'], row['trough'], row['start'], row['end'], row['phase']))
        print("Business cycle data inserted successfully!")
insert_business_cycle_data("financial_data.db")