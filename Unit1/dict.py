# 4.1 Create and access dictionary elements
student = {
    "name": "Mansi",
    "age": 18,
    "course": "Engineering"
}

print("Dictionary:", student)

# Access elements
print("Name:", student["name"])
print("Age:", student.get("age"))

print("\nAll keys:", student.keys())
print("All values:", student.values())

# 4.2 Update Dictionary
student["age"] = 21            # Updating existing value
student["college"] = "XYZ"     # Adding new key-value pair

print("\nUpdated Dictionary:", student)

# 4.3 Removing Elements
student.pop("course")          # Removes 'course'
print("\nAfter removing 'course':", student)

student.popitem()              # Removes last inserted item
print("After popitem():", student)

# 4.4 Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = {**dict1, **dict2}   # Method 1 (Recommended)

print("\nDictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Merged Dictionary:", merged_dict)