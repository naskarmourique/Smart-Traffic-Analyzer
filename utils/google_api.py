import requests

def get_live_traffic(origin, destination, api_key):
    """Call Google Directions API with departure_time=now to get duration_in_traffic.
    Returns simplified dict with duration info and start/end coords.
    origin/destination can be address strings.
    """
    url = (
        "https://maps.googleapis.com/maps/api/directions/json"
        f"?origin={origin}&destination={destination}&departure_time=now&key={api_key}"
    )
    r = requests.get(url)
    data = r.json()
    if data.get('status') != 'OK':
        return {'error': data.get('status')}
    route = data['routes'][0]
    leg = route['legs'][0]
    normal = leg.get('duration', {}).get('text')
    traffic = leg.get('duration_in_traffic', {}).get('text')
    start_loc = leg['start_location']
    end_loc = leg['end_location']
    return {
        'normal_time': normal,
        'traffic_time': traffic,
        'start_location': start_loc,
        'end_location': end_loc,
        'summary': route.get('summary')
    }
