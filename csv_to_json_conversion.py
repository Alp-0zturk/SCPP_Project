import pandas as pd
import json

# Load the CSV file into a DataFrame with the correct delimiter
csv_file = "SCPP_Project/raw_data.csv"  # Replace with your actual file path
df = pd.read_csv(csv_file, delimiter=';')  # Specify the delimiter as ';'

# Convert the DataFrame to JSON, grouping by manufacturer and model
car_data = (
    df.groupby(["manufacturer", "model"])
    .apply(lambda x: {
        "condition": list(x["condition"]),
        "cylinders": list(x["cylinders"]),
        "fuel": list(x["fuel"]),
        "odometer": list(x["odometer"]),
        "title_status": list(x["title_status"]),
        "transmission": list(x["transmission"]),
        "drive": list(x["drive"]),
        "size": list(x["size"]),
        "type": list(x["type"]),
        "paint_color": list(x["paint_color"]),
        "years": list(x["year"]),
        "prices": list(x["price"]),
    })
    .reset_index()
    .groupby("manufacturer")
    .apply(lambda group: {
        "models": [
            {
                "name": model,
                "data": group[group["model"] == model]["0"].values[0],
            }
            for model in group["model"].unique()
        ]
    })
    .to_dict()
)

# Save the resulting JSON to a file
output_file = "car_data.json"
with open(output_file, "w") as json_file:
    json.dump(car_data, json_file, indent=4)

print(f"JSON file saved to {output_file}")
