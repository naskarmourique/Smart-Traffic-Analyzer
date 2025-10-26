# Train a simple RandomForestClassifier to predict congestion_level
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

os.makedirs('models', exist_ok=True)

CSV = 'data/traffic_data.csv'
MODEL_OUT = 'models/predictor.pkl'

if __name__ == '__main__':
    if not os.path.exists(CSV):
        print('Place a CSV at', CSV)
        exit(1)
    df = pd.read_csv(CSV, parse_dates=['ds'] if 'ds' in pd.read_csv(CSV, nrows=1).columns else None)
    # Simple preprocessing
    df['hour'] = df['ds'].dt.hour if 'ds' in df.columns else df.get('hour')
    df['weather_enc'] = df['weather_main'].fillna('Clouds')
    le = LabelEncoder()
    df['weather_enc'] = le.fit_transform(df['weather_enc'])
    if 'congestion_level' not in df.columns:
        print('CSV must include congestion_level (Low/Medium/High)')
        exit(1)
    X = df[['hour','weather_enc','vehicle_count']].fillna(0)
    y = df['congestion_level']
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X,y)
    joblib.dump(model, MODEL_OUT)
    print('Saved model to', MODEL_OUT)
