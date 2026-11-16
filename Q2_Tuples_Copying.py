# Q2: Tuples, Mutability and Copying

print("TUPLES, MUTABILITY AND COPYING")
print("--------------------------------")

# Tuple as dictionary key
student_marks = {
    ("ECE", 101): 85,
    ("ECE", 102): 90,
    ("CSE", 103): 88
}

print("Student marks:", student_marks)

print("\nAccessing tuple key:")
print("ECE 101 Marks:", student_marks[("ECE", 101)])

# Tuple immutability
sample = (10, 20, 30)

print("\nOriginal tuple:", sample)

# Tuple cannot be modified directly
# sample[0] = 50  # This causes an error

# Aliasing
list1 = [10, 20, 30]
list2 = list1

list2[0] = 100

print("\nAliasing:")
print("List 1:", list1)
print("List 2:", list2)

# Shallow copy
original = [[1, 2], [3, 4]]
shallow = original.copy()

shallow[0][0] = 99

print("\nShallow Copy:")
print("Original:", original)
print("Shallow copy:", shallow)

# Manual deep copy without importing modules
original = [[1, 2], [3, 4]]

deep = []

for row in original:
    deep.append(row.copy())

deep[0][0] = 500

print("\nDeep Copy:")
print("Original:", original)
print("Deep copy:", deep)