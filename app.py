from flask import Flask, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import requests
import os
from weather_data import fetch_weather_data, fetch_15_days_weather_data

app = Flask(__name__)
CORS(app)

# Get absolute paths
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'xgboost_model.joblib')
scaler_path = os.path.join(current_dir, 'scaler.joblib')

# Load the model and scaler
try:
    model = joblib.load(model_path)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")

try:
    scaler = joblib.load(scaler_path)
    print("Scaler loaded successfully.")
except Exception as e:
    print(f"Error loading scaler: {e}")

@app.route('/')
def index():
    return "Welcome to the Flask application!"

@app.route('/predict/24hours', methods=['GET'])
def predict_24hours():
    try:
        # Fetch weather data for the next 24 hours
        weather_df = fetch_weather_data(hours_ahead=24)
        print("Fetched weather data for 24 hours:", weather_df.head())

        # Check if weather_df is empty or None
        if weather_df is None or weather_df.empty:
            return jsonify({'error': 'No weather data available'}), 500

        # Extract relevant features
        weather_df['hour'] = weather_df['datetime'].dt.hour
        weather_df['day'] = weather_df['datetime'].dt.day
        weather_df['month'] = weather_df['datetime'].dt.month
        weather_df['year'] = weather_df['datetime'].dt.year
        weather_df['day_of_week'] = weather_df['datetime'].dt.dayofweek

        # Add a dummy mean unrestricted demand (This should be updated with actual logic)
        weather_df['mean_unrestricted_demand'] = 5000  # Placeholder value

        # Select features
        features = ['hour', 'day', 'month', 'year', 'day_of_week', 'temp', 'dwpt', 'rhum', 'prcp', 'wdir', 'wspd', 'pres', 'mean_unrestricted_demand']
        X = weather_df[features]

        # Scale the features
        X_scaled = scaler.transform(X)

        # Make predictions
        predictions = model.predict(X_scaled)

        # Return the predictions
        return jsonify({
            'datetime': weather_df['datetime'].astype(str).tolist(),
            'predictions': predictions.tolist()
        })

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return jsonify({'error': 'Failed to fetch weather data'}), 500
    except ValueError as e:
        print(f"Error processing weather data: {e}")
        return jsonify({'error': 'Error processing weather data'}), 500
    except Exception as e:
        print(f"Unexpected error in /predict/24hours route: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/predict/15days', methods=['GET'])
def predict_15days():
    try:
        # Fetch weather data for the next 15 days
        weather_df = fetch_15_days_weather_data()
        print("Fetched weather data for 15 days:", weather_df.head())

        # Check if weather_df is empty or None
        if weather_df is None or weather_df.empty:
            return jsonify({'error': 'No weather data available'}), 500

        # Extract relevant features
        weather_df['hour'] = weather_df['datetime'].dt.hour
        weather_df['day'] = weather_df['datetime'].dt.day
        weather_df['month'] = weather_df['datetime'].dt.month
        weather_df['year'] = weather_df['datetime'].dt.year
        weather_df['day_of_week'] = weather_df['datetime'].dt.dayofweek

        # Add a dummy mean unrestricted demand (This should be updated with actual logic)
        weather_df['mean_unrestricted_demand'] = 5000  # Placeholder value

        # Select features
        features = ['hour', 'day', 'month', 'year', 'day_of_week', 'temp', 'dwpt', 'rhum', 'prcp', 'wdir', 'wspd', 'pres', 'mean_unrestricted_demand']
        X = weather_df[features]

        # Scale the features
        X_scaled = scaler.transform(X)

        # Make predictions
        predictions = model.predict(X_scaled)

        # Return the predictions
        return jsonify({
            'datetime': weather_df['datetime'].astype(str).tolist(),
            'predictions': predictions.tolist()
        })

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return jsonify({'error': 'Failed to fetch weather data'}), 500
    except ValueError as e:
        print(f"Error processing weather data: {e}")
        return jsonify({'error': 'Error processing weather data'}), 500
    except Exception as e:
        print(f"Unexpected error in /predict/15days route: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

