import os
import psycopg2
import time
import pandas as pd

time.sleep(15)

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="mydatabase",
    user="user",
    password="password",
    host="postgres"
)
cur = conn.cursor()

# Create table if it doesn't exist
CREATE_TABLE_QUERY = '''
CREATE TABLE IF NOT EXISTS stock_data (
    id SERIAL PRIMARY KEY,
    date DATE,
    open FLOAT,
    high FLOAT,
    low FLOAT,
    close FLOAT,
    volume BIGINT,
    stock_symbol VARCHAR(10)
);
'''
cur.execute(CREATE_TABLE_QUERY)
conn.commit()

# Load data from file
DATA_PATH = '/app/data/raw/QQQ.csv'
df = pd.read_csv(DATA_PATH, index_col='Date')
print(df)

for index, row in df.iterrows():
    cur.execute(
        "INSERT INTO stock_data (date, open, high, low, close, volume, stock_symbol) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (index, row['Open'], row['High'], row['Low'], row['Close'], row['Volume'], row['stock_symbol'])
    )

conn.commit()
cur.close()
conn.close()
