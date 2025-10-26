import joblib
import numpy as np
import os

MODEL_PATH = 'models/predictor.pkl'

# For simplicity, we create a simple mapping for weather categories; in real training use one-hot encoding
WEATHER_MAP = {
    'Clear': 0,
    'Clouds': 1,
    'Rain': 2,
    'Drizzle': 2,
    'Thunderstorm': 3,
    'Snow': 4,
    'Mist': 5,
}


def _encode_weather(weather_main):
    return WEATHER_MAP.get(weather_main, 1)


def predict_congestion(hour, weather_main, vehicles):
    # If model exists load it else provide a naive rule-based fallback
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
        x = np.array([[hour, _encode_weather(weather_main), vehicles]])
        pred = model.predict(x)[0]
        return pred
    # fallback rule-based
    score = 0
    if vehicles > 100: score += 2
    if hour in [7,8,9,17,18,19]: score += 2
    w = _encode_weather(weather_main)
    if w in [2,3]: score += 1
    if score >= 4:
        return 'High'
    elif score >= 2:
        return 'Medium'
    return 'Low'
