import pandas as pd
from datetime import datetime, timedelta
import os

alerts = []
base_time = datetime.now()
for i in range(10):
    alert_time = (base_time + timedelta(hours=i)).strftime('%Y-%m-%d %H:%M')
    message = f"Avoid Route {chr(65+i)} between {7+i%12}-{8+i%12} AM/PM due to heavy congestion"
    alerts.append({'time': alert_time, 'message': message})

os.makedirs('database', exist_ok=True)
df = pd.DataFrame(alerts)
df.to_csv('database/alerts.csv', index=False)
print('Dummy alerts.csv generated with', len(df), 'rows.')
