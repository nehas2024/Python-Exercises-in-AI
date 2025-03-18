# Write a program that asks the user to enter a number and checks if it is positive, negative, or zero.

# Algorithm:
# 1. Start
# 2. Prompt the user to enter a number.
# 3. Convert the input to an integer and store it in a variable.
# 4. Check if the number is greater than zero:
#    - If true, print "The number is positive."
# 5. Else, check if the number is less than zero:
#    - If true, print "The number is negative."
# 6. Else:
#    - Print "The number is zero."
# 7. End

a = int(input("Enter a number: "))

if a > 0:
    print("The number is positive.")
elif a < 0:
    print("The number is negative.")
else:
    print("The number is zero.")