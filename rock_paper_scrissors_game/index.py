# This is a simple Rock, Paper, Scissors game in Python
import random                                                              # random number generator

while True:
    print("\nWelcome to the game of Rock, Paper, Scissors!")               # Welcome message

    computer = random.choice([-1, 0, 1])                                   # generate a random choice for the computer

    youstr = input("Enter your choice (Rock, Paper, Scissors): ").lower()  # user input

    dict = {                                                               # Dictionary to convert string to numbers
        "rock": -1,
        "paper": 0,
        "scissors": 1
    }

    rev_dict = {                                                           # Dictionary to convert numbers back to strings
        -1: "rock",
        0: "paper",
        1: "scissors"
    }

    if youstr not in dict:                                                 # Check for valid input
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    you = dict[youstr]                                                     # Convert user input to number

    print("You chose:", youstr)                                            # Show user's choice
    print("Computer chose:", rev_dict[computer])                           # Show computer's choice

    if you == computer:                                                    # Check for draw
        print("It's a draw!")
    else:
        if (you == -1 and computer == 1) or (you == 0 and computer == -1) or (you == 1 and computer == 0):  # User wins
            print("You win!")
        else:                                                              # User loses
            print("You lose!")
            print("Better luck next time!")

    print("Thanks for playing!")                                           # Thank you message

    play_again = input("Do you want to play again? (y/n): ").lower()       # Ask to play again
    if play_again != "y":                                                  # Exit if not 'y'
        print("Goodbye!")
        break

#end of the program