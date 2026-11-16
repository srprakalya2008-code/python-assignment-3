# Q5: Cleaning Sensor Readings

print("CLEANING SENSOR READINGS")
print("-------------------------")

readings = [-60, -20, 0, 5, 10, 15, 25, 40, 60, 100]

print("Original Sensor Readings:")
print(readings)

# Remove invalid readings
cleaned = [x for x in readings if -50 <= x <= 50]

print("\nCleaned Readings:")
print(cleaned)

# Convert Celsius to Fahrenheit
fahrenheit = [(x * 9/5) + 32 for x in cleaned]

print("\nTemperature in Fahrenheit:")
print(fahrenheit)

# Identify alarm readings
alarm_readings = [x for x in cleaned if x < 2 or x > 8]

print("\nAlarm Readings:")
print(alarm_readings)

# Normal readings
normal_readings = [x for x in cleaned if 2 <= x <= 8]

print("\nNormal Readings:")
print(normal_readings)

# Create dictionary using list comprehension
reading_status = {
    x: "ALARM" if x < 2 or x > 8 else "NORMAL"
    for x in cleaned
}

print("\nReading Status:")

for temperature, status in reading_status.items():
    print(temperature, ":", status)

# Unique readings using set comprehension
unique_readings = {x for x in readings if -50 <= x <= 50}

print("\nUnique Valid Readings:")
print(unique_readings)