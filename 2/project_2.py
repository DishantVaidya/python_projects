import time
import random

#typing test 

#sample sentences for the typing test
sentences = [
"Python programming is an excellent skill to learn because it opens the door to many career opportunities in technology, data science, web development, automation, and artificial intelligence, helping you solve real-world problems efficiently."
,"Consistent typing practice improves not only your speed but also your accuracy and confidence. By dedicating time each day to this skill, you can enhance your productivity and communicate more effectively through writing."
,"Developing strong coding habits early in your learning journey makes complex concepts easier to understand. With patience and dedication, you can build projects that showcase your skills and contribute to meaningful innovations."
,"Technology evolves rapidly, so staying updated with new programming languages, tools, and frameworks is essential. Learning continuously helps you adapt, innovate, and remain competitive in the ever-changing digital landscape."
,"Breaking problems into smaller, manageable parts is a key strategy in programming. This approach allows you to focus on solving one piece at a time, leading to cleaner, more efficient code and faster debugging."
]

#random sentence selection
random_sentence = random.choice(sentences)

#user input
print("Type the following sentence under 60 seconds:")
print(random_sentence)
input("Press Enter...")

#time tracking
start_time = time.time()
user_input = input("Start typing: ")
end_time = time.time()

#calculate time taken
total_time = end_time - start_time

#calculate total words typed
total_words = len(user_input.split())

#calculate accuracy
wpm = (total_words/(total_time/60))

#results
if (random_sentence==user_input):
    print("Congratulations! You passed...")
    print(f"Total time taken: {total_time:.2f} seconds")
    print(f"Total words typed: {total_words}")
    print(f"Your typing speed is {wpm:.2f} words per minute.")
else:   
    print("You failed ! Try again....")
