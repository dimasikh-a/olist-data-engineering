import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim

# =====================
# PROJECT ROOT SETUP
# =====================
ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

RAW_PATH = os.path.join(
    ROOT_DIR, "data", "raw", "olist_customers_dataset.csv"
)

PROCESSED_PATH = os.path.join(
    ROOT_DIR, "data", "processed", "dim_customer"
)

print("ROOT_DIR:", ROOT_DIR)
print("RAW_PATH:", RAW_PATH)
print("PROCESSED_PATH:", PROCESSED_PATH)

# =====================
# SPARK SESSION
# =====================
spark = (
    SparkSession.builder
    .appName("Transform dim_customer")
    .master("local[*]")
    .getOrCreate()
)


customers = spark.read.option("header", True).csv(RAW_PATH)


customers_clean = (
    customers
    .select(
        col("customer_id"),
        col("customer_unique_id"),
        col("customer_zip_code_prefix"),
        trim(col("customer_city")).alias("customer_city"),
        col("customer_state")
    )
    .dropna(subset=["customer_id"])
)

customers_clean.show(5)
print("Total customers:", customers_clean.count())

customers_clean.write \
    .mode("overwrite") \
    .parquet("data/processed/dim_customer")


print("✅ dim_customer CSV created successfully")

spark.stop()
