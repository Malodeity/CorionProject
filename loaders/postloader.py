import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os
import sys

print("🔄 Starting stock_market_data upload script...")

# Load environment variables
print("🔍 Loading environment variables...")
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    print("❌ Error: DATABASE_URL not found in .env file.")
    sys.exit(1)

# Load CSV file
try:
    print("📂 Loading stock_market_data CSV...")
    stock_df = pd.read_csv("/Users/malo/Downloads/archive-2/full_stock_df.csv")
    print(f"✅ Loaded {len(stock_df)} rows from full_stock_df.csv")
except FileNotFoundError as e:
    print(f"❌ File not found: {e}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error loading CSV: {e}")
    sys.exit(1)

# Filter to start after record 245500
start_index = 319000
if start_index >= len(stock_df):
    print(f"⚠️ Start index {start_index} exceeds available rows ({len(stock_df)}). Exiting.")
    sys.exit(0)
stock_df = stock_df.iloc[start_index:]

# Connect to PostgreSQL
print("🔌 Connecting to PostgreSQL database...")
try:
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    print("✅ Successfully connected to the database.")
except Exception as e:
    print(f"❌ Failed to connect to database: {e}")
    sys.exit(1)

# Insert into stock_market_data
print(f"📤 Uploading data to stock_market_data starting from record {start_index}...")
try:
    for i, row in stock_df.iterrows():
        cursor.execute("""
            INSERT INTO stock_market_data (Date, Open, High, Low, Close, Adj_Close, Volume, Name, Company_Name)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (Date, Name) DO NOTHING
        """, (
            row['Date'], row['Open'], row['High'], row['Low'], row['Close'],
            row['Adj Close'], row['Volume'], row['Name'], row['Company Name']
        ))

        # Commit every 500 records
        if (i + 1) % 500 == 0:
            conn.commit()
            print(f"  💾 Committed {start_index + i + 1} rows to stock_market_data...")

    # Final commit for remaining rows
    conn.commit()
    print("  ✅ Final commit for stock_market_data complete.")

except Exception as e:
    print(f"❌ Error inserting into stock_market_data: {e}")
    conn.rollback()
    cursor.close()
    conn.close()
    sys.exit(1)

# Close connection
cursor.close()
conn.close()
print("✅ Data upload complete and connection closed.")