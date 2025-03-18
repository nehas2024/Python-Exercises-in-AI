# 1. Program: Find the Factorial of a Number

# Write a program that asks the user for a number and calculates its factorial.
# (The factorial of a number n is the product of all positive integers less than or equal to n).

a = int(input("Enter a number: "))

factorial = 1
n = a

while n >= 1:
    factorial *= n
    n -= 1

print("The factorial of", a, "is:", factorial)