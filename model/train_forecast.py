from utils.forecasting import train_forecast_model

if __name__ == '__main__':
    m = train_forecast_model('data/traffic_data.csv')
    print('Trained SARIMA forecast model and saved')
