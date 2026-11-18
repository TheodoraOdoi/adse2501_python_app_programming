"""
Python Sets
A set is a built in data type that represents an unordered collection of elements of the same
or different types.
Sets DON'T allow duplicates but are mutable and are useful for tasks that involve checking membership,
removing duplicates, and performing mathematical set operations like
intersection, union, difference, and symmetric difference.
Sets are created using the curly braces/brackets {} or the set() constructor.
Some set operations are given below:
"""

# Create a set of fruits
fruits = {"apple", "banana", "cherry",'durian','elephant apple'}

# Display the contents of the fruit set
print(f"The contents of the 'fruits' set are:\n{fruits}")

# Display the number of fruits in the fruit set
print(f"The number of fruits in the  set is: {len (fruits)}")

# Add 'orange' to the set of fruits
fruits.add("orange")
print(f"After adding 'orange' to the set of 'fruits' we get:\n{fruits}")

# Remove 'banana' from the set of fruits
fruits.remove("banana") # Remove throws a KeyError when element is not found
print(f"After removing 'banana' from the set of 'fruits' we get:\n{fruits}")

# Discard 'cherry' from the set of fruits
fruits.discard("cherry") # Discard does nothing (fails silently) when element is not found
print(f"After discarding 'cherry' from the set of 'fruits' we get:\n{fruits}")

# Remove the last fruit from the fruit set
popped_fruit = fruits.pop()
print(f"After popping '{popped_fruit}' from the set of 'fruits' we get:\n{fruits}")

# Declare another set of fruits
more_fruits = {'pear', "avocado","mango",'pineapple'}

# Create a combined set of fruits and display it
combined_fruits = fruits.union(more_fruits)
print(f"The combined set of fruits is:\n{combined_fruits}")

# Copy the remaining set of original fruits and display them
copy_of_fruits = fruits.copy()
print(f"The copy of 'fruits' is:\n{copy_of_fruits}")

# Get and display common fruits in a) 'fruits' & 'more_fruits'. b) 'fruits' & 'combined_fruits'
print(f"The common fruits in a) 'fruits' & 'more_fruits' are: {fruits.intersection(more_fruits)}"
      f"The common fruits in b) 'fruits' & 'combined_fruits' are: {fruits.intersection(combined_fruits)}")

# Get and display fruits in a) 'fruits' but not in 'more_fruits'. b) 'fruits' but not in 'combined_fruits'
print(f"The fruits in a) 'fruits' but not in 'more_fruits' are: {fruits.difference(more_fruits)}"
      f"The fruits in b) 'fruits' but not in 'combined_fruits' are: {fruits.difference(combined_fruits)}")

# Check whether 'combined_fruits' is a superset of 'fruits' set
print(f"'combined_fruits' is a superset of the 'fruits' set: {combined_fruits.issuperset(fruits)}")
# Check whether 'more_fruits' is a superset of 'fruits' set
print(f"'more_fruits' is a superset of the 'fruits' set: {more_fruits.issuperset(fruits)}")

# Check whether 'fruits' is a subset of 'combined_fruits'  set
print(f"'fruits' is a subset of the 'combined_fruits' set: {fruits.issubset(combined_fruits)}")
# Check whether 'fruits' is a subset of 'more_fruits' set
print(f"'fruits' is a subset of the 'more_fruits' set: {fruits.issubset(more_fruits)}")

# Check and display whether 'fruits' set and 'more_fruits' sets have no common fruits/elements
is_disjoint_fruits = fruits.isdisjoint(more_fruits)
print(f"'fruit' set and 'more_fruit'  have no common fruits/elements: {is_disjoint_fruits}")

# Create another fruit set and use it to update the set of 'fruits'. CAUTION...overwrites set elements
other_fruits = {'watermelon', 'strawberry', 'blueberry'}
fruits.update(other_fruits)
print(f"After updating the 'fruit' set we get:\n{fruits}")

# Clear and display the 'fruits' set
fruits.clear()
print(f'After clearing the "fruits" set we get:\n{fruits}')