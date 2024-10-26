import sqlite3

conn = sqlite3.connect('weather_data.db')
c = conn.cursor()

# Fetch all data from the weather_data table
c.execute('SELECT * FROM weather_data')
rows = c.fetchall()

# Print the stored data
for row in rows:
    print(row)

conn.close()