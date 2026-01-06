from pyspark.sql import SparkSession

def create_spark_session():
    return (
        SparkSession.builder
        .appName("Olist Data Engineering")
        .config("spark.sql.shuffle.partitions", "4")
        .getOrCreate()
    )
