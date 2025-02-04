# Creating a list
my_list = [10, 20, 30, 40, 50]

# 1. append() - Add an item at the end
my_list.append(60)
print("After append:", my_list)  # Output: [10, 20, 30, 40, 50, 60]

# 2. extend() - Add multiple items
my_list.extend([70, 80])
print("After extend:", my_list)  # Output: [10, 20, 30, 40, 50, 60, 70, 80]

# 3. insert() - Insert an item at a specific index
my_list.insert(2, 25)
print("After insert:", my_list)  # Output: [10, 20, 25, 30, 40, 50, 60, 70, 80]

# 4. remove() - Remove first occurrence of a value
my_list.remove(30)
print("After remove:", my_list)  # Output: [10, 20, 25, 40, 50, 60, 70, 80]

# 5. pop() - Remove and return an item (default: last)
last_item = my_list.pop()
print("After pop:", my_list, "| Popped item:", last_item)  
# Output: [10, 20, 25, 40, 50, 60, 70] | Popped item: 80

# 6. index() - Find index of an item
index_of_50 = my_list.index(50)
print("Index of 50:", index_of_50)  # Output: 4

# 7. count() - Count occurrences of an item
count_20 = my_list.count(20)
print("Count of 20:", count_20)  # Output: 1

# 8. sort() - Sort the list
my_list.sort()
print("After sort:", my_list)  # Output: [10, 20, 25, 40, 50, 60, 70]

# 9. reverse() - Reverse the list
my_list.reverse()
print("After reverse:", my_list)  # Output: [70, 60, 50, 40, 25, 20, 10]

# 10. copy() - Create a shallow copy
new_list = my_list.copy()
print("Copied list:", new_list)  # Output: [70, 60, 50, 40, 25, 20, 10]

# 11. clear() - Remove all items
my_list.clear()
print("After clear:", my_list)  # Output: []
