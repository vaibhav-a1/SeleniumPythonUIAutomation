import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Define the JSON structure
json_data =

# Function to generate mock data based on data type
def generate_mock_data(column_name, num_records=10):
    if "Decimal" in column_name:
        return np.round(np.random.uniform(1.0, 100.0, num_records), 2)
    elif "String" in column_name:
        return [f"SampleText{i}" for i in range(num_records)]
    elif "Integer" in column_name:
        return np.random.randint(1, 100, num_records)
    elif "Date" in column_name:
        base_date = datetime.today()
        return [(base_date - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(num_records)]
    else:
        return [f"Data{i}" for i in range(num_records)]

# Process each table and column
tables = {}
for entry in json_data:
    for mapping in entry:
        table_name = mapping["table"]
        column_name = mapping["column"]

        if table_name not in tables:
            tables[table_name] = {}

        tables[table_name][column_name] = generate_mock_data(column_name)

# Create CSV files for each table
for table_name, columns in tables.items():
    df = pd.DataFrame(columns)
    csv_filename = f"{table_name}.csv"
    df.to_csv(csv_filename, index=False)
    print(f"CSV file created: {csv_filename}")