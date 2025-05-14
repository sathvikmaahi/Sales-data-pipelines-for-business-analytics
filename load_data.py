# load/load_data.py
from sqlalchemy import create_engine

def load_to_postgres(df, table_name="sales", db_url="postgresql://user:pass@localhost:5432/etl_project"):
    engine = create_engine(db_url)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
