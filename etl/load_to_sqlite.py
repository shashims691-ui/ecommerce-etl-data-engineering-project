import os
import sqlite3
import pandas as pd

# -------------------------------------------------
# Project Paths
# -------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_FOLDER = os.path.join(BASE_DIR, "data")
DATABASE_FOLDER = os.path.join(BASE_DIR, "database")
DATABASE_PATH = os.path.join(DATABASE_FOLDER, "ecommerce.db")

os.makedirs(DATABASE_FOLDER, exist_ok=True)

# -------------------------------------------------
# Gold Layer CSV Files
# -------------------------------------------------
csv_files = {
    "dim_customer": "dim_customer.csv",
    "dim_product": "dim_product.csv",
    "dim_seller": "dim_seller.csv",
    "fact_orders": "fact_orders.csv",
    "fact_payments": "fact_payments.csv",
    "fact_reviews": "fact_reviews.csv",
    "fact_delivery_sla": "fact_delivery_sla.csv"
}

# -------------------------------------------------
# Connect SQLite
# -------------------------------------------------
conn = sqlite3.connect(DATABASE_PATH)

print("=" * 60)
print("Loading Gold Layer Tables into SQLite")
print("=" * 60)

for table_name, file_name in csv_files.items():

    file_path = os.path.join(DATA_FOLDER, file_name)

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    print(f"✔ {table_name} loaded successfully")
    print(f"Rows Loaded : {len(df)}")
    print("-" * 60)

conn.close()

print("\nDatabase Created Successfully")
print("Database Location :", DATABASE_PATH)