### **Problem:**  
# Write a program that asks the user for two numbers and an operator (`+`, `-`, `*`, `/`) and performs the operation.  


### **Algorithm:**  
# 1. **Start**  
# 2. **Input** two numbers from the user and store them in variables `a` and `b`.  
# 3. **Input** an operator (`+`, `-`, `*`, `/`) from the user and store it in variable `c`.  
# 4. **Check** the operator:  
#    - If `c` is `+`, perform addition (`a + b`) and store the result in `d`.  
#    - Else if `c` is `-`, perform subtraction (`a - b`) and store the result in `d`.  
#    - Else if `c` is `*`, perform multiplication (`a * b`) and store the result in `d`.  
#    - Else if `c` is `/`:  
#      - If `b` is not zero, perform division (`a / b`) and store the result in `d`.  
#      - Otherwise, print an error message (`"Error! Division by zero is not allowed."`).  
#    - Else, print `"Invalid operator!"`.  
# 5. **Display** the result stored in `d`.  
# 6. **End**  

# Taking input from the user
a = int(input("Enter first number: "))
b = int(input("Enter the second number: "))
c = input("Enter the operator (+, -, *, /): ")

# Performing the operation based on user input
if c == '+':
    d = a + b
elif c == '-':
    d = a - b
elif c == '*':
    d = a * b
elif c == '/':
    if b != 0:  # Checking to avoid division by zero
        d = a / b
    else:
        d = "Error! Division by zero is not allowed."
else:
    d = "Invalid operator!"

# Displaying the result
print("The result is:", d)
