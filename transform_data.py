import pandas as pd

def transform_data(df):
    # Drop missing values
    df = df.dropna()

    # Convert order_date to datetime
    df['order_date'] = pd.to_datetime(df['order_date'])

    # Standardize string fields
    df['region'] = df['region'].str.title().str.strip()
    df['product'] = df['product'].str.title().str.strip()
    df['customer_name'] = df['customer_name'].str.title().str.strip()

    # Total price in USD
    df['total_price_usd'] = df['unit_price'] * df['quantity']

    # Convert to INR
    conversion_rate = 83
    df['total_price_inr'] = df['total_price_usd'] * conversion_rate

    # Grouped Revenue by Region and Product
    grouped = df.groupby(['region', 'product'])['total_price_usd'].sum().reset_index()
    grouped = grouped.rename(columns={'total_price_usd': 'revenue_by_product_region_usd'})

    # Merge it into the main DataFrame
    df = df.merge(grouped, on=['region', 'product'], how='left')

    return df
