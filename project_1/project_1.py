import random #random number generator

# Start of the game
print("Welcome to the game of Rock, Paper, Scissors!")

computer = random.choice([-1, 0, 1]) #generate a random choice for the computer
youstr = input("Enter your choice (rock, paper, scissors): ").lower()  #user will input their choice and it will be converted to lowercase


# Dictionary to convert string to numbers
dict = {
    "rock": -1,
    "paper": 0,
    "scissors": 1
}

# Dictionary to convert numbers back to strings
rev_dict = {
    -1: "rock",
    0: "paper",
    1: "scissors"
}

you = dict[youstr]

#prints the choices made by the user and the computer
print("You chose:", youstr)
print("Computer chose:", rev_dict[computer])

# Logic for checking the winner
if(you == computer):
    print("It's a draw!")  

else:
    if(you==-1 and computer==1) or (you==0 and computer==-1) or (you==1 and computer==0): # Check if the user wins in all cases else the computer wins
        print("You win!")
    else:
        print("You lose!")
        print("Better luck next time!")

print("Thanks for playing!")
# End of the game
