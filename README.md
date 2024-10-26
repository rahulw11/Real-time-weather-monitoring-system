# Real-Time Weather Monitoring System

This project is a real-time weather monitoring and data processing system that continuously retrieves weather data from the OpenWeatherMap API for major Indian cities, performs data rollups and aggregates, and generates alerts based on user-defined thresholds. The application is built to monitor weather patterns and generate insights from summarized data.

Features:

    Weather Data Collection: Periodically fetches weather data for specified cities.
    Temperature Conversion: Converts temperature values from Kelvin to Celsius.
    Daily Summaries: Calculates daily summaries, including average, max, and min temperatures, along with the dominant weather condition.
    Alerting Mechanism: Generates alerts when specific thresholds (e.g., temperature exceeding 35°C) are breached.
    Configurable Scheduling: Allows flexible scheduling for data fetching, summary calculations, and alert checks.

Project Structure:

    main_scheduler.py: Manages task scheduling for fetching weather data, calculating daily summaries, and checking alerts.
    weather_data.py: Handles fetching data from OpenWeatherMap API and storing it in a SQLite database.
    view_weather_data.py: Provides a way to view saved weather data from the database.
    rollups_aggregates.py: Calculates daily weather summaries.
    alerts.py: Checks for and triggers alerts when thresholds are breached.

Prerequisites:

    Python 3.x
    SQLite
    OpenWeatherMap API key (sign up at OpenWeatherMap for a free API key)

Dependencies:

    Install necessary packages:
    pip install requests schedule

Setup Instructions:

    Clone the Repository:
    git clone https://github.com/rahulw11/Real-time-weather-monitoring-system.git
    cd Real-time-weather-monitoring-system

Set Up Environment Variables:

    Store your API key in weather_data.py:
    API_KEY = 'your_openweathermap_api_key'  #you can use your own API key

Run the Scheduler:

    python main_scheduler.py

View Weather Data:

    To view saved weather data, run:
    python view_weather_data.py

Usage:

1. Real-Time Data Fetching:

    main_scheduler.py continuously fetches weather data at 5-minute intervals for cities: Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad.
    Modify main_scheduler.py to adjust the scheduling frequency.

2. Calculating Daily Summaries:

    Summaries are calculated daily at midnight.
    Daily aggregates include:
        Average Temperature: Mean of all temperature readings for the day.
        Maximum/Minimum Temperature: Highest and lowest temperatures of the day.
        Dominant Weather Condition: The most frequently observed weather condition for the day.

3. Alerting:
   
    Alerts are checked hourly.
    Example alert: Temperature exceeds 35°C for two consecutive updates.
    Modify alerts.py to configure custom alert thresholds.

Database Storage:

    Weather data is stored in an SQLite database (weather_data.db).
    Schema:
        Table weather_data:
            city (TEXT): Name of the city.
            temperature (REAL): Current temperature in Celsius.
            feels_like (REAL): Perceived temperature in Celsius.
            condition (TEXT): Main weather condition (e.g., Clear, Rain).
            humidity (INTEGER): Humidity percentage.
            wind_speed (REAL): Wind speed in m/s.
            timestamp (TEXT): Data retrieval timestamp.

Example Scenarios:

    Data Retrieval:
        fetch_all_weather retrieves and stores weather data every 5 minutes.
        Check for updates in weather_data.db.
        
    Daily Summary:
        Run calculate_daily_summary() in rollups_aggregates.py to summarize daily data.
    Alerts:
        Run check_alerts() in alerts.py to trigger alerts if thresholds are breached.

Test Cases:

    System Setup:
        Verify that the system starts successfully and connects to OpenWeatherMap API using a valid API key.
        
    Data Retrieval:
        Simulate API calls at intervals to verify the correct data is fetched and stored.
        
    Temperature Conversion:
        Test temperature conversions from Kelvin to Celsius to ensure accuracy.
        
    Daily Summary Calculation:
        Simulate several days of data and verify the daily summaries (average, min, max temperatures).
        
    Alerting Thresholds:
        Define temperature thresholds and simulate data that exceeds them.
        Verify that alerts trigger when thresholds are breached.

Configuration:

    Modify scheduling intervals in main_scheduler.py.
    Adjust alert thresholds in alerts.py.
    Add or change cities in weather_data.py (cities list).

Future Enhancements:

    Extend to additional weather parameters, such as pressure, visibility.
    Implement email notifications for alerts.
    Add visualization for daily summaries and alert history.


![weather](https://github.com/user-attachments/assets/201ec5a5-9452-40bd-b00b-d93c3a867836)
![weather2](https://github.com/user-attachments/assets/f514b0f7-fb9f-4e2f-8bc0-3e1699792cfd)
