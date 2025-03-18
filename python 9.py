# Write a program that takes a list of numbers and finds the maximum number.

# Prompt the user to enter numbers separated by spaces
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Find the maximum number in the list
max_number = max(numbers)

# Print the maximum number
print("The maximum number is:", max_number)

