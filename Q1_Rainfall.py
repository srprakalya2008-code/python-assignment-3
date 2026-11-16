# Q1: Daily Rainfall Records

rainfall = [12, 0, 5, 18, 25, 0, 8,
            10, 15, 0, 20, 30, 12, 5,
            0, 7, 14, 22, 0, 9, 16]

print("DAILY RAINFALL RECORDS")
print("----------------------")

print("Rainfall readings:", rainfall)

# Total rainfall
total = sum(rainfall)
print("\nTotal rainfall:", total, "mm")

# Wettest day
wettest = max(rainfall)
print("Highest rainfall:", wettest, "mm")
print("Wettest day:", rainfall.index(wettest) + 1)

# Driest day
driest = min(rainfall)
print("Lowest rainfall:", driest, "mm")
print("Driest day:", rainfall.index(driest) + 1)

# Average rainfall
average = total / len(rainfall)
print("Average rainfall:", round(average, 2), "mm")

# First seven days
print("\nFirst seven days:", rainfall[:7])

# Last seven days
print("Last seven days:", rainfall[-7:])

# Moving average for seven days
print("\nSeven-day moving averages:")

for i in range(len(rainfall) - 6):
    week = rainfall[i:i + 7]
    avg = sum(week) / 7
    print("Days", i + 1, "to", i + 7, ":", round(avg, 2))

# Dry days
dry_days = []

for i in range(len(rainfall)):
    if rainfall[i] == 0:
        dry_days.append(i + 1)

print("\nDry days:", dry_days)
print("Number of dry days:", len(dry_days))