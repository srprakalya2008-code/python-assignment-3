# Q6: Railway Timetable

print("RAILWAY TIMETABLE")
print("------------------")

timetable = {
    "Train101": {
        "name": "Chennai Express",
        "source": "Chennai",
        "destination": "Bangalore",
        "departure": "06:00",
        "arrival": "12:00"
    },

    "Train102": {
        "name": "Pandian Express",
        "source": "Madurai",
        "destination": "Chennai",
        "departure": "07:00",
        "arrival": "14:00"
    },

    "Train103": {
        "name": "Coimbatore Express",
        "source": "Chennai",
        "destination": "Coimbatore",
        "departure": "08:00",
        "arrival": "15:00"
    },

    "Train104": {
        "name": "Bangalore Express",
        "source": "Bangalore",
        "destination": "Chennai",
        "departure": "09:00",
        "arrival": "16:00"
    },

    "Train105": {
        "name": "Salem Express",
        "source": "Chennai",
        "destination": "Salem",
        "departure": "10:00",
        "arrival": "14:00"
    }
}

# Display complete timetable
print("\nComplete Railway Timetable:")

for train_id, details in timetable.items():
    print("\nTrain ID:", train_id)

    for key, value in details.items():
        print(key, ":", value)

# Search trains from Chennai
print("\nTrains Departing from Chennai:")

for train_id, details in timetable.items():
    if details["source"] == "Chennai":
        print(train_id, "-", details["name"])

# Search trains to Chennai
print("\nTrains Arriving at Chennai:")

for train_id, details in timetable.items():
    if details["destination"] == "Chennai":
        print(train_id, "-", details["name"])

# Sort trains based on departure time
sorted_trains = sorted(
    timetable.items(),
    key=lambda item: item[1]["departure"]
)

print("\nTrains Sorted by Departure Time:")

for train_id, details in sorted_trains:
    print(train_id, details["name"], details["departure"])