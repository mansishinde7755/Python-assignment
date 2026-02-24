# Python program to perform operations on Lists

# 1.1 Create and access list elements
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)

print("First element:", my_list[0])
print("Last element:", my_list[-1])

# 1.2 Add and Remove list elements
my_list.append(60)      # Adding element
print("After adding 60:", my_list)

my_list.remove(30)      # Removing element
print("After removing 30:", my_list)

# 1.3 Sort list elements
my_list.sort()
print("Sorted List:", my_list)

# 1.4 Reverse list elements
my_list.reverse()
print("Reversed List:", my_list)