from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "Shashikanth",
    "start_date": datetime(2026, 6, 19),
    "retries": 1,
}

with DAG(
    dag_id="ecommerce_etl_pipeline",
    default_args=default_args,
    schedule=None,
    catchup=False,
    description="Load Gold Layer CSV files into SQLite Database",
) as dag:

    load_gold_tables = BashOperator(
        task_id="load_gold_tables",
        bash_command="""
        cd /workspaces/Hero-airflow-project &&
        python etl/load_to_sqlite.py
        """
    )

    load_gold_tables