import sqlite3
import pandas as pd

# Database name
db_name = "financial_data.db"

# Connect to the database
conn = sqlite3.connect(db_name)

# Fetch and print the economic indicators data
economic_indicators_query = "SELECT * FROM economic_indicators"
economic_indicators_df = pd.read_sql(economic_indicators_query, conn)
print("Economic Indicators:\n", economic_indicators_df.head(30))

# Fetch and print the yield curve data
yield_curve_prices_query = "SELECT * FROM yield_curve_prices"
yield_curve_prices_df = pd.read_sql(yield_curve_prices_query, conn)
print("\nYield Curve Data:\n", yield_curve_prices_df.head())

# Fetch data from business_cycles table
business_cycles_query = "SELECT * FROM business_cycles"
business_cycles_df = pd.read_sql(business_cycles_query, conn)
print("\nBusiness Cycles Data:\n", business_cycles_df.head())

# Close the database connection
conn.close()