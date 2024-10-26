import requests
import sqlite3
from datetime import datetime

API_KEY = 'e81600cd876b3c40b9057e5fa1cda55e'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

# Database setup
conn = sqlite3.connect('weather_data.db')
c = conn.cursor()

# Drop the old table (run this only once if you want to delete old data)
c.execute('DROP TABLE IF EXISTS weather_data')

# Recreate the table with 7 columns
c.execute('''CREATE TABLE IF NOT EXISTS weather_data (
                city TEXT, 
                temperature REAL, 
                feels_like REAL, 
                condition TEXT, 
                humidity INTEGER, 
                wind_speed REAL,
                timestamp TEXT)''')
conn.commit()


def fetch_weather(city):
    params = {
        'q': city,
        'appid': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        main_weather = data['weather'][0]['main']
        temp_kelvin = data['main']['temp']
        feels_like_kelvin = data['main']['feels_like']
        humidity = data['main']['humidity']  # Extracting humidity
        wind_speed = data['wind']['speed']   # Extracting wind speed

        # Convert temperature from Kelvin to Celsius
        temp_celsius = temp_kelvin - 273.15
        feels_like_celsius = feels_like_kelvin - 273.15
        
        # Get the current timestamp
        current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Save to database with humidity and wind speed
        c.execute('INSERT INTO weather_data VALUES (?, ?, ?, ?, ?, ?, ?)',
                  (city, temp_celsius, feels_like_celsius, main_weather, humidity, wind_speed, current_timestamp))
        conn.commit()

        # Print the output to the console
        print(f"City: {city}")
        print(f"Temperature: {temp_celsius:.2f}°C")
        print(f"Feels Like: {feels_like_celsius:.2f}°C")
        print(f"Weather Condition: {main_weather}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Timestamp: {current_timestamp}")
        print('-' * 30)  # Separator for readability
    else:
        print(f"Failed to fetch data for {city}. Error: {response.status_code}")


def fetch_all_weather():
    for city in cities:
        fetch_weather(city)

# Fetch weather data for all cities
fetch_all_weather()


# Close the database connection
conn.close()
