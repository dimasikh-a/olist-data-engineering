import sys
import os


ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
sys.path.insert(0, ROOT_DIR)


from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Olist Data Engineering")
    .master("local[*]")
    .config("spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version", "2")
    .config("spark.sql.sources.commitProtocolClass",
            "org.apache.spark.sql.execution.datasources.SQLHadoopMapReduceCommitProtocol")
    .config("spark.sql.parquet.output.committer.class",
            "org.apache.parquet.hadoop.ParquetOutputCommitter")
    .config("spark.hadoop.fs.file.impl.disable.cache", "true")
    .getOrCreate()
)

jdbc_url = "jdbc:postgresql://localhost:5432/olist_dw"
properties = {
    "user": "postgres",
    "password": "postgres",
    "driver": "org.postgresql.Driver"
}

df = spark.read.parquet("data/processed/dim_customer")

df.write.jdbc(
    url=jdbc_url,
    table="dim_customer",
    mode="overwrite",
    properties=properties
)

print("dim_customer loaded successfully")
