# 2.1 Create and access set elements
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

print("\nAccessing elements of Set 1:")
for element in set1:
    print(element)

# 2.2 Union of the elements
union_set = set1.union(set2)
print("\nUnion of Set1 and Set2:", union_set)

# 2.3 Intersection of the elements
intersection_set = set1.intersection(set2)
print("Intersection of Set1 and Set2:", intersection_set)

# 2.4 Difference of the elements
difference_set1 = set1.difference(set2)
difference_set2 = set2.difference(set1)

print("Difference (Set1 - Set2):", difference_set1)
print("Difference (Set2 - Set1):", difference_set2)