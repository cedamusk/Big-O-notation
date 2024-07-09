

# Create an array of integers
my_array = [1, 2, 3, 4, 5]

# Print the length of the array (O(1) - constant time)
print("Length of the array:", len(my_array))

# Append an element to the end of the array (O(1) - amortized constant time)
my_array.append(6)
print("Array after appending:", my_array)

# Insert an element at a specific index (O(n) - worst case linear time)
my_array.insert(2, 99)
print("Array after inserting at index 2:", my_array)

# Access an element by index (O(1) - constant time)
first_element = my_array[0]
print("First element:", first_element)

# Loop through the array and print each element (O(n) - linear time)
for element in my_array:
  print(element)
