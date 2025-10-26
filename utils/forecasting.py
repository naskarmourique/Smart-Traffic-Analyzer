import joblib
import pandas as pd
import os
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Note: The model is no longer a Prophet model, but we keep the name for compatibility with the calling code.
# A better long-term solution would be to rename the file and update references.
MODEL_FILE = 'models/forecast_model.pkl' 

def train_forecast_model(csv_path='data/traffic_data.csv'):
    """
    Trains a SARIMA model and saves it.
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Data file not found at {csv_path}")
    
    df = pd.read_csv(csv_path, parse_dates=['ds'], index_col='ds')
    
    # We need a continuous time series. Resample to hourly frequency and fill any missing values.
    y = df['vehicle_count'].resample('H').mean().fillna(method='ffill')

    # Define the SARIMA model. These are standard parameters for hourly data with a daily seasonality.
    # (p,d,q): Non-seasonal order
    # (P,D,Q,m): Seasonal order (m=24 for daily seasonality on hourly data)
    model = SARIMAX(y,
                    order=(1, 1, 1),
                    seasonal_order=(1, 1, 0, 24),
                    enforce_stationarity=False,
                    enforce_invertibility=False)
    
    results = model.fit()
    
    joblib.dump(results, MODEL_FILE)
    print(f"SARIMA model trained and saved to {MODEL_FILE}")
    return results

def forecast_next_day():
    """
    Loads the trained SARIMA model and forecasts the next 24 hours.
    """
    if not os.path.exists(MODEL_FILE):
        if os.path.exists('data/traffic_data.csv'):
            print("Model not found. Training a new one...")
            train_forecast_model()
        else:
            # Return an empty DataFrame if no data is available to train
            return pd.DataFrame(columns=['ds', 'yhat', 'yhat_lower', 'yhat_upper'])

    model_results = joblib.load(MODEL_FILE)
    
    # Forecast the next 24 steps
    forecast = model_results.get_forecast(steps=24)
    
    # Get the predicted values and confidence intervals
    yhat = forecast.predicted_mean
    conf_int = forecast.conf_int()
    
    # Create a DataFrame in the format expected by the frontend
    forecast_df = pd.DataFrame({
        'ds': yhat.index,
        'yhat': yhat.values,
        'yhat_lower': conf_int.iloc[:, 0].values,
        'yhat_upper': conf_int.iloc[:, 1].values
    })
    
    return forecast_df
