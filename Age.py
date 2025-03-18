#Take input from the user
a = int(input("Enter your age: "))
nationality = input("Are you a citizen of India? (yes/no): ")

if a >= 18 and nationality.lower() == "yes":
    print("You are eligible to vote.")
elif a < 18 and nationality.lower() == "yes":
    print("You are a minor.")
else:
    print("You are not a citizen.")


