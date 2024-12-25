import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error
import numpy as np

# Load the dataset
df = pd.read_csv('vehicles-random-subset-ThisOne-minMaxNorm.csv')
data = pd.read_csv('vehicles-random-subset-ThisOne-minMaxNorm.csv')

# Data Cleaning
# Remove rows with missing price or odometer values
data = data.dropna(subset=['price', 'odometer'])

# Filter out unrealistic prices
data = data[(data['price'] > 500) & (data['price'] < 100000)]

# Select features and target
features = [
    'year', 'manufacturer', 'model', 'condition', 'cylinders', 'fuel', 'odometer',
    'title_status', 'transmission', 'drive', 'size', 'type', 'paint_color'
]
target = 'price'

X = data[features]
y = data[target]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing pipeline
numeric_features = ['year', 'odometer']
numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

categorical_features = [
    'manufacturer', 'model', 'condition', 'cylinders', 'fuel', 'title_status',
    'transmission', 'drive', 'size', 'type', 'paint_color'
]
categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

# Define the model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Create the pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', model)
])

# Train the model
pipeline.fit(X_train, y_train)

# Make predictions
y_pred = pipeline.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"Root Mean Squared Error: {rmse}")



mape = mean_absolute_percentage_error(y_test, y_pred)

print(f"Mean Absolute Percentage Error (MAPE): {mape:.2%}")


# Example input for prediction
example_input = pd.DataFrame([{
    'year': 2015,
    'manufacturer': 'toyota',
    'model': 'corolla',
    'condition': 'excellent',
    'cylinders': '4 cylinders',
    'fuel': 'gas',
    'odometer': 60000,
    'title_status': 'clean',
    'transmission': 'automatic',
    'drive': 'fwd',
    'size': 'compact',
    'type': 'sedan',
    'paint_color': 'white'
}])

# Predict the price for the example input
predicted_price = pipeline.predict(example_input)
print(f"Predicted Price: ${predicted_price[0]:,.2f}")
