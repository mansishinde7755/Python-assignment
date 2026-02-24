# 3.1 Create and access tuple
tuple1 = (10, 20, 30, 40, 50)

print("Tuple:", tuple1)

# Access elements
print("First element:", tuple1[0])
print("Last element:", tuple1[-1])

print("\nAccessing all elements:")
for item in tuple1:
    print(item)

# 3.2 Nested Tuple
nested_tuple = ("Apple", "Banana", (1, 2, 3), "Mango")

print("\nNested Tuple:", nested_tuple)
print("Element inside nested tuple:", nested_tuple[2][1])  # Access 2 from (1,2,3)

# 3.3 Repetition of tuple
repeated_tuple = tuple1 * 2
print("\nRepeated Tuple:", repeated_tuple)

# 3.4 Concatenation of tuples
tuple2 = (60, 70, 80)
concatenated_tuple = tuple1 + tuple2

print("\nConcatenated Tuple:", concatenated_tuple)