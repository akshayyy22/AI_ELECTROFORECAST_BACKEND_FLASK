# import requests
# import pandas as pd
# from datetime import datetime, timedelta

# # Replace with your API key
# API_KEY = 'VUTE5VQL5MCH2S9M3HY9N8LJD'
# LOCATION = 'Delhi,IN'

# def fetch_weather_data(hours_ahead=24):
#     URL = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{LOCATION}?unitGroup=metric&key={API_KEY}&include=hours&contentType=json'

#     # Fetch weather data
#     response = requests.get(URL)
#     data = response.json()

#     weather_data = []
#     hours_collected = 0
#     current_time = datetime.now()

#     for day in data['days']:
#         for entry in day['hours']:
#             if hours_collected >= hours_ahead:
#                 break

#             # Get the full datetime string for each hour entry
#             time_str = entry['datetime']
#             date_str = day['datetime']
#             full_datetime_str = f"{date_str}T{time_str}"
#             entry_datetime = datetime.strptime(full_datetime_str, '%Y-%m-%dT%H:%M:%S')

#             # Only collect data from the current time onward
#             if entry_datetime >= current_time:
#                 weather_data.append({
#                     'datetime': entry_datetime,
#                     'temp': entry['temp'],
#                     'dwpt': entry['dew'],  # Dew point
#                     'rhum': entry['humidity'],
#                     'prcp': entry['precip'],
#                     'wdir': entry['winddir'],
#                     'wspd': entry['windspeed'],
#                     'pres': entry['pressure']
#                 })

#                 hours_collected += 1
#         if hours_collected >= hours_ahead:
#             break

#     # Convert to DataFrame
#     weather_df = pd.DataFrame(weather_data)
#     return weather_df

# def fetch_30_days_weather_data():
#     days_data = []

#     for i in range(30):
#         date = (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d')
#         URL = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{LOCATION}/{date}?unitGroup=metric&key={API_KEY}&include=hours&contentType=json'
        
#         response = requests.get(URL)
#         day_data = response.json()
        
#         for entry in day_data['days'][0]['hours']:
#             entry_datetime = datetime.strptime(f"{date}T{entry['datetime']}", '%Y-%m-%dT%H:%M:%S')
#             days_data.append({
#                 'datetime': entry_datetime,
#                 'temp': entry['temp'],
#                 'dwpt': entry['dew'],
#                 'rhum': entry['humidity'],
#                 'prcp': entry['precip'],
#                 'wdir': entry['winddir'],
#                 'wspd': entry['windspeed'],
#                 'pres': entry['pressure']
#             })
    
#     days_df = pd.DataFrame(days_data)
#     return days_df
import requests
import pandas as pd
from datetime import datetime, timedelta

# Replace with your API key
API_KEY = 'VUTE5VQL5MCH2S9M3HY9N8LJD'
LOCATION = 'Delhi,IN'

def fetch_weather_data(hours_ahead=24):
    URL = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{LOCATION}?unitGroup=metric&key={API_KEY}&include=hours&contentType=json'

    # Fetch weather data
    response = requests.get(URL)
    data = response.json()

    weather_data = []
    hours_collected = 0
    current_time = datetime.now()

    for day in data['days']:
        for entry in day['hours']:
            if hours_collected >= hours_ahead:
                break

            # Get the full datetime string for each hour entry
            time_str = entry['datetime']
            date_str = day['datetime']
            full_datetime_str = f"{date_str}T{time_str}"
            entry_datetime = datetime.strptime(full_datetime_str, '%Y-%m-%dT%H:%M:%S')

            # Only collect data from the current time onward
            if entry_datetime >= current_time:
                weather_data.append({
                    'datetime': entry_datetime,
                    'temp': entry['temp'],
                    'dwpt': entry['dew'],  # Dew point
                    'rhum': entry['humidity'],
                    'prcp': entry['precip'],
                    'wdir': entry['winddir'],
                    'wspd': entry['windspeed'],
                    'pres': entry['pressure']
                })

                hours_collected += 1
        if hours_collected >= hours_ahead:
            break

    # Convert to DataFrame
    weather_df = pd.DataFrame(weather_data)
    return weather_df

def fetch_15_days_weather_data():
    days_data = []

    for i in range(15):
        date = (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d')
        URL = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{LOCATION}/{date}?unitGroup=metric&key={API_KEY}&include=hours&contentType=json'
        
        response = requests.get(URL)
        day_data = response.json()
        
        for entry in day_data['days'][0]['hours']:
            entry_datetime = datetime.strptime(f"{date}T{entry['datetime']}", '%Y-%m-%dT%H:%M:%S')
            days_data.append({
                'datetime': entry_datetime,
                'temp': entry['temp'],
                'dwpt': entry['dew'],
                'rhum': entry['humidity'],
                'prcp': entry['precip'],
                'wdir': entry['winddir'],
                'wspd': entry['windspeed'],
                'pres': entry['pressure']
            })
    
    days_df = pd.DataFrame(days_data)
    return days_df
