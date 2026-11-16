# Q3: Farmer Helpline Complaint Analysis

print("FARMER HELPLINE COMPLAINT ANALYSIS")
print("-----------------------------------")

complaints = [
    "Seeds not received",
    "Water supply problem",
    "Seeds quality issue",
    "Fertilizer not received",
    "Water supply problem",
    "Seeds not received",
    "Crop price issue"
]

# Word frequency dictionary
word_count = {}

for complaint in complaints:
    words = complaint.lower().split()

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

print("\nWord Frequency:")

for word, count in word_count.items():
    print(word, ":", count)

# Remove common words
stop_words = ["not", "the", "is", "a"]

filtered_count = {}

for word, count in word_count.items():
    if word not in stop_words:
        filtered_count[word] = count

print("\nFiltered Word Frequency:")

for word, count in filtered_count.items():
    print(word, ":", count)

# Find top three words
sorted_words = sorted(
    filtered_count.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\nTop Three Words:")

for word, count in sorted_words[:3]:
    print(word, ":", count)

# District-wise complaint grouping
district_complaints = {}

data = [
    ("Chennai", "Water supply problem"),
    ("Madurai", "Seeds not received"),
    ("Chennai", "Fertilizer issue"),
    ("Salem", "Crop price issue"),
    ("Madurai", "Water supply problem")
]

for district, complaint in data:
    district_complaints.setdefault(district, []).append(complaint)

print("\nDistrict-wise Complaints:")

for district, complaint_list in district_complaints.items():
    print(district, ":", complaint_list)