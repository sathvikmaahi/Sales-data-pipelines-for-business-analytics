# main.py
from extract.extract_data import extract_data
from transform.transform_data import transform_data
from load.load_data import load_to_postgres  # or load_to_bigquery

def run_etl():
    df = extract_data()
    transformed_df = transform_data(df)
    load_to_postgres(transformed_df)

if __name__ == "__main__":
    run_etl()
