# from flask import Flask, jsonify
# import joblib
# import pandas as pd
# from weather_data import fetch_weather_data, fetch_30_days_weather_data
# import os
# import logging

# # Initialize Flask app
# app = Flask(__name__)

# # Set up logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# # Get absolute paths
# current_dir = os.path.dirname(os.path.abspath(__file__))
# model_path = os.path.join(current_dir, 'xgboost_model.joblib')
# scaler_path = os.path.join(current_dir, 'scaler.joblib')

# # Load the model and scaler
# try:
#     model = joblib.load(model_path)
#     scaler = joblib.load(scaler_path)
# except Exception as e:
#     logger.error(f"Error loading model or scaler: {e}")
#     raise

# @app.route('/predict/24hours', methods=['GET'])
# def predict_24hours():
#     try:
#         # Fetch weather data for the next 24 hours
#         weather_df = fetch_weather_data(hours_ahead=24)
        
#         # Ensure datetime column is in the correct format
#         weather_df['datetime'] = pd.to_datetime(weather_df['datetime'])
        
#         # Extract relevant features
#         weather_df['hour'] = weather_df['datetime'].dt.hour
#         weather_df['day'] = weather_df['datetime'].dt.day
#         weather_df['month'] = weather_df['datetime'].dt.month
#         weather_df['year'] = weather_df['datetime'].dt.year
#         weather_df['day_of_week'] = weather_df['datetime'].dt.dayofweek

#         # Add a dummy mean unrestricted demand (Update with actual logic if available)
#         weather_df['mean_unrestricted_demand'] = 3000  # Placeholder value

#         # Select features
#         features = ['hour', 'day', 'month', 'year', 'day_of_week', 'temp', 'dwpt', 'rhum', 'prcp', 'wdir', 'wspd', 'pres', 'mean_unrestricted_demand']
#         X = weather_df[features]

#         # Scale the features
#         X_scaled = scaler.transform(X)

#         # Make predictions
#         predictions = model.predict(X_scaled)

#         # Return the predictions
#         return jsonify({
#             'datetime': weather_df['datetime'].astype(str).tolist(),
#             'predictions': predictions.tolist()
#         })
#     except Exception as e:
#         logger.error(f"Error in /predict/24hours: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/predict/30days', methods=['GET'])
# def predict_30days():
#     try:
#         # Fetch weather data for the next 30 days
#         weather_df = fetch_30_days_weather_data()
        
#         # Ensure datetime column is in the correct format
#         weather_df['datetime'] = pd.to_datetime(weather_df['datetime'])
        
#         # Extract relevant features
#         weather_df['hour'] = weather_df['datetime'].dt.hour
#         weather_df['day'] = weather_df['datetime'].dt.day
#         weather_df['month'] = weather_df['datetime'].dt.month
#         weather_df['year'] = weather_df['datetime'].dt.year
#         weather_df['day_of_week'] = weather_df['datetime'].dt.dayofweek

#         # Add a dummy mean unrestricted demand (Update with actual logic if available)
#         weather_df['mean_unrestricted_demand'] = 3000  # Placeholder value

#         # Select features
#         features = ['hour', 'day', 'month', 'year', 'day_of_week', 'temp', 'dwpt', 'rhum', 'prcp', 'wdir', 'wspd', 'pres', 'mean_unrestricted_demand']
#         X = weather_df[features]

#         # Scale the features
#         X_scaled = scaler.transform(X)

#         # Make predictions
#         predictions = model.predict(X_scaled)

#         # Return the predictions
#         return jsonify({
#             'datetime': weather_df['datetime'].astype(str).tolist(),
#             'predictions': predictions.tolist()
#         })
#     except Exception as e:
#         logger.error(f"Error in /predict/30days: {e}")
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, jsonify
# import joblib
# import pandas as pd
# from weather_data import fetch_weather_data, fetch_30_days_weather_data

# app = Flask(__name__)

# # Get absolute paths
# import os
# current_dir = os.path.dirname(os.path.abspath(__file__))
# model_path = os.path.join(current_dir, 'xgboost_model.joblib')
# scaler_path = os.path.join(current_dir, 'scaler.joblib')

# # Load the model and scaler
# try:
#     model = joblib.load(model_path)
#     print("Model loaded successfully.")
# except Exception as e:
#     print(f"Error loading model: {e}")

# try:
#     scaler = joblib.load(scaler_path)
#     print("Scaler loaded successfully.")
# except Exception as e:
#     print(f"Error loading scaler: {e}")

# @app.route('/')
# def index():
#     return "Welcome to the Flask application!"

# @app.route('/predict/24hours', methods=['GET'])
# def predict_24hours():
#     # Fetch weather data for the next 24 hours
#     weather_df = fetch_weather_data(hours_ahead=24)

#     # Extract relevant features
#     weather_df['hour'] = weather_df['datetime'].dt.hour
#     weather_df['day'] = weather_df['datetime'].dt.day
#     weather_df['month'] = weather_df['datetime'].dt.month
#     weather_df['year'] = weather_df['datetime'].dt.year
#     weather_df['day_of_week'] = weather_df['datetime'].dt.dayofweek

#     # Add a dummy mean unrestricted demand (This should be updated with actual logic)
#     weather_df['mean_unrestricted_demand'] = 5000  # Placeholder value

#     # Select features
#     features = ['hour', 'day', 'month', 'year', 'day_of_week', 'temp', 'dwpt', 'rhum', 'prcp', 'wdir', 'wspd', 'pres', 'mean_unrestricted_demand']
#     X = weather_df[features]

#     # Scale the features
#     X_scaled = scaler.transform(X)

#     # Make predictions
#     predictions = model.predict(X_scaled)

#     # Return the predictions
#     return jsonify({
#         'datetime': weather_df['datetime'].astype(str).tolist(),
#         'predictions': predictions.tolist()
#     })


# @app.route('/predict/30days', methods=['GET'])
# def predict_30days():
#     try:
#         # Fetch weather data for the next 30 days
#         weather_df = fetch_30_days_weather_data()
#         print("Weather data fetched successfully.")

#         # Extract relevant features
#         weather_df['hour'] = weather_df['datetime'].dt.hour
#         weather_df['day'] = weather_df['datetime'].dt.day
#         weather_df['month'] = weather_df['datetime'].dt.month
#         weather_df['year'] = weather_df['datetime'].dt.year
#         weather_df['day_of_week'] = weather_df['datetime'].dt.dayofweek

#         # Add a dummy mean unrestricted demand (This should be updated with actual logic)
#         weather_df['mean_unrestricted_demand'] = 5000  # Placeholder value

#         # Select features
#         features = ['hour', 'day', 'month', 'year', 'day_of_week', 'temp', 'dwpt', 'rhum', 'prcp', 'wdir', 'wspd', 'pres', 'mean_unrestricted_demand']
#         X = weather_df[features]

#         # Scale the features
#         X_scaled = scaler.transform(X)

#         # Make predictions
#         predictions = model.predict(X_scaled)

#         # Return the predictions
#         return jsonify({
#             'datetime': weather_df['datetime'].astype(str).tolist(),
#             'predictions': predictions.tolist()
#         })
#     except Exception as e:
#         print(f"Error in /predict/30days route: {e}")
#         return jsonify({'error': 'Internal Server Error'}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, jsonify
import joblib
import pandas as pd
from weather_data import fetch_weather_data, fetch_15_days_weather_data

app = Flask(__name__)

# Get absolute paths
import os
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
    # Fetch weather data for the next 24 hours
    weather_df = fetch_weather_data(hours_ahead=24)

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

@app.route('/predict/15days', methods=['GET'])
def predict_15days():
    try:
        # Fetch weather data for the next 15 days
        weather_df = fetch_15_days_weather_data()
        print("Weather data fetched successfully.")

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
    except Exception as e:
        print(f"Error in /predict/15days route: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
