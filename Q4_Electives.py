# Q4: Elective Registration Clash Detection

print("ELECTIVE REGISTRATION CLASH DETECTION")
print("--------------------------------------")

student1 = {"IoT", "VLSI", "AI", "Robotics"}

student2 = {"AI", "Cloud Computing", "VLSI", "Python"}

print("Student 1 Electives:", student1)
print("Student 2 Electives:", student2)

# Common electives
common = student1.intersection(student2)

print("\nCommon Electives:")
print(common)

# All available electives
all_electives = student1.union(student2)

print("\nAll Electives:")
print(all_electives)

# Electives selected only by Student 1
only_student1 = student1.difference(student2)

print("\nOnly Student 1:")
print(only_student1)

# Electives selected only by Student 2
only_student2 = student2.difference(student1)

print("\nOnly Student 2:")
print(only_student2)

# Electives selected by either student, but not both
unique_electives = student1.symmetric_difference(student2)

print("\nUnique Electives:")
print(unique_electives)

# Clash detection
if len(common) > 0:
    print("\nElective Clash Detected!")
else:
    print("\nNo Elective Clash Detected.")