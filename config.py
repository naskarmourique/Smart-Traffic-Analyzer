import os
from dotenv import load_dotenv
load_dotenv()

GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
DATABASE = 'database/traffic.db'
