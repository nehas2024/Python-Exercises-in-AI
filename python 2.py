# Write a program that takes a number from the user and checks if it is even or odd.

# algo:-
# 1. input a number from the user.
# 2. divide the number by 2.if the modulus is 0 then the number is even otherwise odd.

a = int(input("Enter a number : "))

if (a % 2) == 0:
 print(a, "is an even number ")

else:
 print(a, "is an odd number ")

