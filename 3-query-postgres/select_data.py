import os
import psycopg2
import time
import pandas as pd

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),  # Use the host machine's IP address
    port=os.getenv("DB_PORT", "5432")
)
cur = conn.cursor()

# select query
SELECT_QUERY = '''
SELECT * FROM stock_data;
'''
cur.execute(SELECT_QUERY)

rows = cur.fetchall()


# Get column names from the cursor
colnames = [desc.name for desc in cur.description]
# Create a DataFrame from the fetched data
df = pd.DataFrame(rows, columns=colnames)
print(df)

# Close communication with the database
cur.close()
conn.close()
