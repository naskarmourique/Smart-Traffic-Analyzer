import requests

def get_weather_for_coords(lat, lon, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}'
    r = requests.get(url)
    if r.status_code != 200:
        return {'error': r.status_code}
    data = r.json()
    weather = {
        'main': data['weather'][0]['main'],
        'description': data['weather'][0]['description'],
        'temp': data['main']['temp'],
        'humidity': data['main']['humidity']
    }
    return weather
