import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
import joblib

# Load your dataset
data = pd.read_csv('final.csv')

# Convert 'date' and 'time' columns to a single datetime column
data['datetime'] = pd.to_datetime(data['date'] + ' ' + data['time'])

# Extract useful date-related features
data['hour'] = data['datetime'].dt.hour
data['day'] = data['datetime'].dt.day
data['month'] = data['datetime'].dt.month
data['year'] = data['datetime'].dt.year
data['day_of_week'] = data['datetime'].dt.dayofweek

# Group by year and month and calculate mean unrestricted demand
monthly_mean = data.groupby(['year', 'month'])['unrestricted_demand'].mean().reset_index()
monthly_mean.rename(columns={'unrestricted_demand': 'mean_unrestricted_demand'}, inplace=True)

# Merge the monthly mean back into the original data
data = pd.merge(data, monthly_mean, on=['year', 'month'], how='left')

# Select features for prediction (including weather data and calculated mean unrestricted demand)
features = ['hour', 'day', 'month', 'year', 'day_of_week', 'temp', 'dwpt', 'rhum', 'prcp', 'wdir', 'wspd', 'pres', 'mean_unrestricted_demand']

# Define target variable
target = 'unrestricted_demand'

# Split data into features (X) and target (y)
X = data[features]
y = data[target]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Initialize the scaler
scaler = StandardScaler()

# Fit the scaler on the training data and transform both training and test data
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize the XGBoost Regressor
model = xgb.XGBRegressor(
    objective='reg:squarederror',  # For regression tasks
    n_estimators=100,              # Number of trees
    learning_rate=0.1,             # Learning rate
    max_depth=5,                   # Maximum depth of a tree
    random_state=42                # For reproducibility
)

# Train the model
model.fit(X_train_scaled, y_train)

# Save the model and scaler
joblib.dump(model, 'xgboost_model.joblib')
joblib.dump(scaler, 'scaler.joblib')
