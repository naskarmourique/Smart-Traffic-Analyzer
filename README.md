# 🚦 Smart Traffic Analyzer & Predictor

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/release/python-311/) [![Flask](https://img.shields.io/badge/Flask-2.3-black.svg)](https://flask.palletsprojects.com/) [![Scikit-learn](https://img.shields.io/badge/SciKit--Learn-1.3-orange.svg)](https://scikit-learn.org/) [![Pandas](https://img.shields.io/badge/Pandas-2.1-blue.svg)](https://pandas.pydata.org/)

A full-stack web application that analyzes historical traffic data, predicts congestion using machine learning, and displays live traffic conditions on an interactive map.

---

## ✨ Key Features

- **🗺️ Live Interactive Map**: View real-time traffic conditions and routes using the Google Maps API.
- **📈 Predictive Modeling**: Predicts congestion levels ("Low", "Medium", "High") based on time, weather, and vehicle count using a Scikit-learn model.
- **🔮 24-Hour Forecasting**: Forecasts vehicle counts for the next 24 hours using a SARIMA time-series model.
- **📊 Data Analysis Dashboard**: Upload a CSV of historical traffic data to generate and view insightful plots and summary statistics.
- **🌤️ Weather Integration**: Fetches and displays live weather data from the OpenWeatherMap API for the route's origin.
- **Modern UI**: A clean, responsive, and modern dark-themed UI with loading indicators for a smooth user experience.

---


## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Data Science**: Pandas, NumPy, Scikit-learn, Statsmodels
- **APIs**: Google Maps Directions API, OpenWeatherMap API
- **Visualization**: Matplotlib, Seaborn

---

## ⚙️ Setup and Installation

### Prerequisites
- **Python 3.11**. This project has dependencies that require Python 3.11. Using other versions may cause installation errors.
- **Google Maps & OpenWeatherMap API Keys**.

### 1. Clone the Repository
```bash
git clone https://github.com/naskarmourique/Smart-Traffic-Analyzer.git
cd Smart-Traffic-Analyzer
```

### 2. Create a Virtual Environment
It is crucial to use a virtual environment with **Python 3.11**.

```bash
# Replace with the path to your Python 3.11 executable if it's not the default
python -m venv venv
```

Activate the environment:
```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Keys
Create a file named `.env` in the root of the project and add your API keys:
```
GOOGLE_MAPS_API_KEY=your_google_maps_key_here
OPENWEATHER_API_KEY=your_openweathermap_key_here
SECRET_KEY=a_strong_secret_key_here
```

---

## 🚀 Usage

### 1. Train the Models (First-time setup)
Before running the app for the first time, you need to train the ML models using the included dummy data.

```bash
# Train the prediction model
python model\train_model.py

# Train the forecast model
python -m model.train_forecast
```

### 2. Run the Application
```bash
flask run
```
The application will be available at `http://127.0.0.1:5000`.

---

## 🗂️ Project Structure
```
.
├── app.py                # Main Flask application
├── config.py             # Configuration for API keys
├── requirements.txt      # Project dependencies
├── .env                  # File for API keys (must be created)
├── generate_dummy_...py  # Scripts to create sample data
│
├── data/
│   └── traffic_data.csv  # Dummy traffic data
│
├── database/
│   └── alerts.csv        # Dummy alerts data
│
├── models/
│   ├── predictor.pkl     # Trained ML model for prediction
│   └── forecast_model.pkl  # Trained model for forecasting
│
├── static/
│   ├── css/style.css     # Main stylesheet
│   └── js/main.js        # JavaScript for loading indicators
│
└── templates/
    ├── base.html         # Base layout template
    ├── index.html        # Home page
    ├── live.html         # Live traffic map page
    └── ...               # Other HTML pages
```
