from flask import Flask, render_template, request, redirect, url_for, flash
import os
import logging
from utils.google_api import get_live_traffic
from utils.weather_api import get_weather_for_coords
from utils.prediction import predict_congestion
from utils.forecasting import forecast_next_day, train_forecast_model
from utils.data_analysis import save_plots_from_df, summarize_data
from config import GOOGLE_MAPS_API_KEY, OPENWEATHER_API_KEY, SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Configure logging
logging.basicConfig(level=logging.INFO)


UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        f = request.files.get('file')
        if not f:
            flash('No file uploaded')
            return redirect(url_for('index'))
        path = os.path.join(UPLOAD_FOLDER, f.filename)
        f.save(path)
        app.logger.info(f'File uploaded and saved to {path}')
        imgs = save_plots_from_df(path)
        summary = summarize_data(path)
        return render_template('dashboard.html', images=imgs, summary=summary)
    return redirect(url_for('index'))

@app.route('/live', methods=['GET', 'POST'])
def live():
    # form fields: origin, destination
    if request.method == 'POST':
        origin = request.form.get('origin')
        destination = request.form.get('destination')
        api_key = GOOGLE_MAPS_API_KEY
        if not api_key:
            app.logger.error('Google Maps API key not configured')
            flash('Google Maps API key not configured')
            return redirect(url_for('index'))
        app.logger.info(f'Fetching live traffic from {origin} to {destination}')
        data = get_live_traffic(origin, destination, api_key)
        # get weather for origin coords if available
        coords = data.get('start_location')
        weather = None
        if coords and OPENWEATHER_API_KEY:
            weather = get_weather_for_coords(coords['lat'], coords['lng'], OPENWEATHER_API_KEY)
        return render_template('live.html', traffic=data, weather=weather, api_key=api_key)
    return redirect(url_for('index'))

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    result = None
    if request.method == 'POST':
        hour = int(request.form.get('hour'))
        weather_main = request.form.get('weather')
        vehicles = int(request.form.get('vehicle_count'))
        result = predict_congestion(hour=hour, weather_main=weather_main, vehicles=vehicles)
    return render_template('predict.html', result=result)

@app.route('/forecast', methods=['GET'])
def forecast():
    # show 24-hour forecast
    forecast_df = forecast_next_day()
    # convert to list of dicts for template
    rows = forecast_df.to_dict('records')
    return render_template('forecast.html', rows=rows)

@app.route('/alerts')
def alerts():
    # for starter: read alerts file if exists
    alerts_file = 'database/alerts.csv'
    alerts = []
    if os.path.exists(alerts_file):
        import pandas as pd
        alerts = pd.read_csv(alerts_file).to_dict('records')
    return render_template('alerts.html', alerts=alerts)

if __name__ == '__main__':
    app.run(debug=True)
