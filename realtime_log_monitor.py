import time
import random
import pandas as pd

# Thresholds
TEMP_THRESHOLD = 40.0  # °C
HUMIDITY_THRESHOLD = 80.0  # %

# Log file path
LOG_FILE = "sensor_log.csv"

# Initialize log
df_log = pd.DataFrame(columns=["Timestamp", "Temperature", "Humidity", "Status"])
df_log.to_csv(LOG_FILE, index=False)

def get_sensor_data():
    # Simulated sensor readings
    temperature = round(random.uniform(20, 50), 2)
    humidity = round(random.uniform(30, 90), 2)
    return temperature, humidity

# Main loop
try:
    print("🔍 Monitoring sensors in real-time. Press Ctrl+C to stop.\n")
    while True:
        temp, humidity = get_sensor_data()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        status = "NORMAL"

        if temp > TEMP_THRESHOLD or humidity > HUMIDITY_THRESHOLD:
            status = "ALERT 🚨"
            print(f"[{timestamp}] ALERT: Temp={temp}°C, Humidity={humidity}%")

        else:
            print(f"[{timestamp}] Temp={temp}°C, Humidity={humidity}%")

        # Log the entry
        df = pd.DataFrame([[timestamp, temp, humidity, status]], columns=df_log.columns)
        df.to_csv(LOG_FILE, mode='a', header=False, index=False)

        time.sleep(2)  # Delay between readings

except KeyboardInterrupt:
    print("\n🛑 Monitoring stopped by user.")
