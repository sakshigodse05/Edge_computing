import time
import random
import pandas as pd

# Simulate sensor data
def read_temperature_sensor():
    return round(random.uniform(20.0, 30.0), 2)  # °C

def read_humidity_sensor():
    return round(random.uniform(40.0, 60.0), 2)  # %

# Fusion function: combines readings from both sensors
def fuse_sensor_data(temp, humidity):
    # Example fusion logic: weighted average (simple)
    comfort_index = round((0.6 * temp + 0.4 * humidity), 2)
    return comfort_index

# Store data
fused_data = []

# Simulate 10 readings
for _ in range(10):
    temp = read_temperature_sensor()
    humidity = read_humidity_sensor()
    comfort = fuse_sensor_data(temp, humidity)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    fused_data.append({
        "Timestamp": timestamp,
        "Temperature (°C)": temp,
        "Humidity (%)": humidity,
        "Comfort Index": comfort
    })

    print(f"[{timestamp}] Temp: {temp}°C, Humidity: {humidity}%, Comfort Index: {comfort}")
    time.sleep(1)  # Simulate 1-second sensor interval

# Convert to DataFrame
df = pd.DataFrame(fused_data)
print("\nFused Data Table:")
print(df)
