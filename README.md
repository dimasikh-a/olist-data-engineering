# Olist Customer Data Engineering Pipeline

## Project Overview
This project implements an end-to-end batch data engineering pipeline
to ingest, transform, and load customer master data into a PostgreSQL
data warehouse using PySpark and Airflow.

## Dataset
The dataset used in this project is `olist_customers_dataset.csv`,
which contains customer master data. Other transactional datasets
were not provided, therefore the pipeline focuses on customer
dimension processing.

## Tech Stack
- Python
- PySpark
- PostgreSQL
- Apache Airflow

## Pipeline Flow
CSV → PySpark (cleaning & standardization) → PostgreSQL → Airflow Scheduler

## Data Quality
- Null check on primary key
- Deduplication on customer_id
- Standardization of city and state

## Output
- dim_customer table ready for analytics

## Limitation
Business-level analytics such as sales and RFM analysis were not
implemented due to the absence of transactional data.
