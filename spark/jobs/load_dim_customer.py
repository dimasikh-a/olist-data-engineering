import os
from pyspark.sql import SparkSession


ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

PROCESSED_PATH = os.path.join(
    ROOT_DIR, "data", "processed", "dim_customer"
)

print("ROOT_DIR:", ROOT_DIR)
print("PROCESSED_PATH:", PROCESSED_PATH)
print("PATH EXISTS:", os.path.exists(PROCESSED_PATH))

spark = (
    SparkSession.builder
    .appName("Load dim_customer")
    .master("local[*]")
    .getOrCreate()
)


df = spark.read.option("header", True).csv(PROCESSED_PATH)

df.show(5)
print("Rows to load:", df.count())


jdbc_url = "jdbc:postgresql://localhost:5432/olist_dw"
properties = {
    "user": "postgres",
    "password": "postgres",
    "driver": "org.postgresql.Driver"
}


df.write.jdbc(
    url=jdbc_url,
    table="dim_customer",
    mode="overwrite",
    properties=properties
)

print("✅ dim_customer loaded successfully to PostgreSQL")

spark.stop()
