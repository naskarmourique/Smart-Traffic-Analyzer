import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate 30 days of hourly data
dates = pd.date_range(start='2025-10-01 00:00', end='2025-10-30 23:00', freq='H')
np.random.seed(42)

vehicle_count = np.random.randint(20, 200, size=len(dates))
avg_speed = np.random.uniform(20, 60, size=len(dates))
weather_options = ['Clear', 'Clouds', 'Rain', 'Drizzle', 'Thunderstorm', 'Snow', 'Mist']
weather_main = np.random.choice(weather_options, size=len(dates))
temperature = np.random.uniform(15, 35, size=len(dates))

# Assign congestion levels
congestion_level = []
for i, count in enumerate(vehicle_count):
    hour = dates[i].hour
    level = 'Low'
    if count > 120 or hour in [7,8,9,17,18,19]:
        level = 'Medium'
    if count > 160:
        level = 'High'
    congestion_level.append(level)

day = [d.strftime('%a') for d in dates]

df = pd.DataFrame({
    'ds': dates,
    'hour': [d.hour for d in dates],
    'day': day,
    'vehicle_count': vehicle_count,
    'avg_speed': avg_speed,
    'weather_main': weather_main,
    'temperature': temperature,
    'congestion_level': congestion_level
})

df.to_csv('data/traffic_data.csv', index=False)
print('Dummy traffic_data.csv generated with', len(df), 'rows.')
