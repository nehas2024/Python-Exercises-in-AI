
# Program: Fibonacci Sequence

# Write a program that generates the first n Fibonacci numbers. Ask the user to enter n and print the sequence up to that number.

n = int(input("Enter a number: "))

a = 0
b = 1

fibonacci_sequence = [a, b]

for _ in range(0, n):
    next_number = a + b
    fibonacci_sequence.append(next_number)
    a = b
    b = next_number

print("The first", n, "Fibonacci numbers are:", fibonacci_sequence)