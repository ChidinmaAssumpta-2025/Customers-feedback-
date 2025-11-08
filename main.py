import os
import pandas as pd
import requests
import io
import psycopg2
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# ==============================
# STEP 1: Load environment variables
# ==============================
load_dotenv()

# Kobo credentials
KOBO_USERNAME = os.getenv("KOBO_USERNAME")
KOBO_PASSWORD = os.getenv("KOBO_PASSWORD")
KOBO_URL = os.getenv("KOBO_URL")

# PostgreSQL credentials
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_DATABASE = os.getenv("PG_DATABASE")

# Schema and table details
schema_name = "Chidinma_1"
table_name = "customers_feedback"

# ==============================
# STEP 2: Fetch data from KoboToolbox
# ==============================
print("📡 Fetching data from KoboToolbox...")
response = requests.get(KOBO_URL, auth=HTTPBasicAuth(KOBO_USERNAME, KOBO_PASSWORD))

if response.status_code != 200:
    print(f"❌ Failed to fetch data. Status code: {response.status_code}")
    exit()

print("✅ Data fetched successfully")

csv_data = io.StringIO(response.text)
df = pd.read_csv(csv_data, sep=';', on_bad_lines='skip')

print("📊 Sample of downloaded data:")
print(df.head(), "\n")

# ==============================
# STEP 3: Connect to PostgreSQL
# ==============================
print("🔗 Connecting to PostgreSQL...")

try:
    conn = psycopg2.connect(
        host=PG_HOST,
        database=PG_DATABASE,
        user=PG_USER,
        password=PG_PASSWORD,
        port=PG_PORT
    )
    conn.autocommit = True
    cur = conn.cursor()
    print("✅ Connection successful!\n")

except Exception as e:
    print(f"❌ Database connection failed: {e}")
    exit()

# ==============================
# STEP 4: Create Schema and Table
# ==============================
cur.execute(f"CREATE SCHEMA IF NOT EXISTS {schema_name};")

cur.execute(f"""
    DROP TABLE IF EXISTS {schema_name}.{table_name};
    CREATE TABLE {schema_name}.{table_name} (
        id SERIAL PRIMARY KEY,
        start TIMESTAMPTZ,
        "end" TIMESTAMPTZ,
        "Date_of_reporting" TEXT,
        "Store_location" TEXT,
        "Gender" TEXT,
        "Age" TEXT,
        "How_satisfied_are_you_with_the_product_pricing" TEXT,
        "How_satisfied_are_you_with_the_customer_services" TEXT,
        "What_is_your_overall_satisfaction" TEXT,
        "what_is_your_recommendation" TEXT,
        "_id" INT,
        "_uuid" TEXT,
        "_submission_time" TIMESTAMPTZ,
        "_validation_status" TEXT,
        "_notes" TEXT,
        "_status" TEXT,
        "_submitted_by" TEXT,
        "__version__" TEXT,
        "_tags" TEXT,
        "_index" INT
    );
""")
print(f"✅ Schema '{schema_name}' and table '{table_name}' created successfully!\n")

# ==============================
# STEP 5: Insert Data
# ==============================
print("🧩 Inserting data into PostgreSQL...")

insert_query = f"""
    INSERT INTO {schema_name}.{table_name} (
        start, "end", "Date_of_reporting", "Store_location", "Gender", "Age",
        "How_satisfied_are_you_with_the_product_pricing",
        "How_satisfied_are_you_with_the_customer_services",
        "What_is_your_overall_satisfaction",
        "what_is_your_recommendation",
        "_id", "_uuid", "_submission_time", "_validation_status", "_notes",
        "_status", "_submitted_by", "__version__", "_tags", "_index"
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

for _, row in df.iterrows():
    cur.execute(insert_query, (
        row.get("start"),
        row.get("end"),
        row.get("Date of reporting"),
        row.get("Store location"),
        row.get("Gender"),
        row.get("Age"),
        row.get("How satisfied are you with the product pricing"),
        row.get("How satisfied are you with the customer services"),
        row.get("What is your overall satisfaction?"),
        row.get("what is your recommendation"),
        row.get("_id"),
        row.get("_uuid"),
        row.get("_submission_time"),
        row.get("_validation_status"),
        row.get("_notes"),
        row.get("_status"),
        row.get("_submitted_by"),
        row.get("__version__"),
        row.get("_tags"),
        row.get("_index"),
    ))

print(f"✅ {len(df)} rows successfully inserted into {schema_name}.{table_name}!")

# ==============================
# STEP 6: Close Connection
# ==============================
cur.close()
conn.close()
print("🎉 All done! Data successfully loaded into PostgreSQL.")
