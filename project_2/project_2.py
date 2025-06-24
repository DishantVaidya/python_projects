import time
import random

# typing test program

# sample sentences for the typing test
sentences = [
"artificial intelligence deep learning neural network programming coding developer algorithms data science cybersecurity cloud computing",
"mountain river forest butterfly adventure hiking camping exploration nature travel wilderness fresh air",
"javascript python programming software engineering website database server api design testing deployment",
"healthy nutrition fitness exercise meditation yoga strength discipline motivation habits productivity routine",
"culture heritage language literature music traditions festivals celebrations cuisine history geography exploration",
"space exploration astronomy universe galaxy stars planets black holes telescopes discovery science technology"
]

# random sentence selection
random_sentence = random.choice(sentences)

# user input
print("Type the following sentence under 60 seconds:")
print(random_sentence)
input("Press Enter...")

# time tracking
start_time = time.time()
user_input = input("Start typing: ")
end_time = time.time()

# calculate time taken
total_time = end_time - start_time

# calculate total words typed
total_words = len(user_input.split())

# calculate accuracy
wpm = (total_words / (total_time / 60))

#timeout condition
if total_time > 60:
    print("You took too long! Try to type faster next time.")

#difficulty condition
diff=input("Do you want to increase the difficulty in accuracy? (yes/no): ").strip().lower()
if diff == 'yes':
    if random_sentence == user_input: # results
     print("Congratulations! You passed...")
     print(f"Total time taken: {total_time:.2f} seconds")
     print(f"Total words typed: {total_words}")
     print(f"Your typing speed is {wpm:.2f} words per minute.")
    else:
     print("You failed ! Try again....")
else:
     print("Congratulations! You passed...")
     print(f"Total time taken: {total_time:.2f} seconds")
     print(f"Total words typed: {total_words}")
     print(f"Your typing speed is {wpm:.2f} words per minute.")

#end of the program 