# Guess the number game
import random  

# Generate a random number between 1 and 50 
n = random.randint(1, 50)
a = -1          #
guess = 0       

# Loop continues until the user's guess matches the generated number
while a != n:
    a = int(input("Guess the number from 1 to 50: "))

    # If the guess is higher than the actual number
    if a > n:
        print(f"Enter a lower number than {a}")
        guess += 1   # Increment the number of attempts

    # If the guess is lower than the actual number
    elif a < n:
        print(f"Enter a higher number than {a}")
        guess += 1   # Increment the number of attempts

# When the guess is correct, display the result
print(f"You correctly guessed the number {n} in {guess} attempts!")
