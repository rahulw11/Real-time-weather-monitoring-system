import schedule
import time
from weather_data import fetch_all_weather
from rollups_aggregates import calculate_daily_summary
from alerts import check_alerts

# Scheduling tasks
schedule.every(5).minutes.do(fetch_all_weather)  # Fetch weather every 5 minutes
schedule.every().day.at("00:00").do(calculate_daily_summary)  # Daily summary at midnight
schedule.every().hour.do(check_alerts)  # Check alerts every hour

while True:
    schedule.run_pending()
    time.sleep(1)