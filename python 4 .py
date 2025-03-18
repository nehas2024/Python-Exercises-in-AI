    # program:- Generate a random number between 1 and 10. Ask the user to guess the number until they get it right.
    

   # algo:-
    # Generate a random number between 1 and 10.
    # Ask the user to guess the number.
    # Keep checking the user's guess until they guess correctly.
    # Print a congratulatory message when the user guesses the correct number.


import random  # Importing the random module

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Start the loop to take guesses from the user
while True:
    a = int(input("Enter a random number between 1 to 10: "))

    if a == number:  # Check if the guessed number is correct
        print("Congratulations! You guessed the right number:", a)
        break  # Exit the loop if the guess is correct
    else:
        print("Good luck for the next guess!")






