# Sales Data ETL Pipeline Project

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline built using Python. It simulates a real-world scenario where sales data is extracted, cleaned and enriched with KPIs, and then loaded for reporting and analytics. It process the raw data and applied transformations for currency conversions.


# Project Summary
This project simulates a retail sales data pipeline, from extraction to final visualization:

Extracts mock sales data from a CSV source (or API-ready structure)

Applies robust transformations, including:
  -Data cleaning
  -Currency conversion (USD ➝ INR)
  -Aggregated revenue metrics by region and product
Loads the final transformed dataset into a destination (CSV/local DB)
Visualizes key performance indicators (KPIs) in a dynamic Streamlit dashboard

## Project Structure

```
sales_etl_project/
│
├── data/               # Contains raw and cleaned data files
├── extract_data.py     # Extract data logic
│  
├── transform_data.py   # Transform logic (cleaning, KPIs)
│ 
├── load_data.py        # Load logic (to CSV or DB)
│   
├── dashboard (app.py)  # Streamlit dashboard app
│  
├── main.py             # Orchestrates the ETL flow
└── README.md           # Project documentation
```

## Tools Used
- Python (Pandas, Streamlit)
- Faker (for data generation)
- CSV files (simulated data source)
- Streamlit (for visualization)

## How to Run the Project

1. **Install Dependencies**
```bash
pip install pandas streamlit
```

2. **Run the ETL Pipeline**
```bash
python main.py
```

3. **Launch the Dashboard**
```bash
streamlit run app.py  
```

## Dashboard Features
- Total revenue KPI
- Revenue by region (bar chart)
- Sales trend over time (line chart)

## Future Enhancements
- Load into a real database like PostgreSQL or BigQuery
- Use Apache Airflow for scheduling
- Add authentication and filtering to the dashboard

## Author
Sathvik Sanka
