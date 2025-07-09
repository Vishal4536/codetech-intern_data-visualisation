import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration
API_KEY = 'your_openweathermap_api_key'  # Replace with your real API key
CITY = 'Chennai'
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetching data
response = requests.get(URL)
data = response.json()

# Parse temperature and date
dates = []
temps = []

for item in data['list']:
    dates.append(item['dt_txt'])
    temps.append(item['main']['temp'])

# Visualization using Seaborn
sns.set(style="darkgrid")
plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=temps, marker='o', color='orange')
plt.title(f"5-Day Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()

# Show plot
plt.show()
