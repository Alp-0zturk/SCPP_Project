import pandas as pd

# Correctly read the CSV file into a DataFrame
df = pd.read_csv("/Users/w/Desktop/SCPP/Data_files/filled_data.csv", names=['year', 'manufacturer', 'model', 'condition', 'cylinders', 'fuel', 'odometer', 'title_status', 'transmission', 'drive', 'size', 'type', 'paint_color', 'price'])

# Convert the 'odometer' column to numeric
df['odometer'] = pd.to_numeric(df['odometer'], errors='coerce')

# Min-max normalization function
def min_max_normalize(column):
    min_val = column.min()
    max_val = column.max()
    normalized_column = (column - min_val) / (max_val - min_val)
    return normalized_column.round(6)  # Round to 6 decimal places

# Normalize the 'odometer' column
df['odometer_normalized'] = min_max_normalize(df['odometer'])

print(df[['odometer', 'odometer_normalized']])