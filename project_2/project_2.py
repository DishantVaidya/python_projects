import time
import random

# typing test

# sample sentences for the typing test
sentences = [
    "The morning sun shines through the window, lighting up the room. A soft breeze moves the leaves outside, making a quiet sound. It is a beautiful day to walk, read a book, or simply relax and enjoy nature.",
    "Learning to code takes time and practice every day. It may seem hard at first, but with patience and focus, you can understand each concept clearly. In the end, it will open many doors to new opportunities.",
    "A long walk in the park is a simple way to refresh the mind and body. The sound of birds, the smell of flowers, and the feeling of fresh air can help reduce stress and make you feel more alert and happy.",
    "Writing is a powerful way to express thoughts, feelings, and ideas. By putting words on paper, you can organize your thoughts, understand yourself better, and share your message with people around the world.",
    "A healthy lifestyle is built from small habits. Eating fresh vegetables, drinking enough water, and sleeping well every night can make a big difference. Gradual changes can lead to lasting results over time.",
    "Time is one of the most precious things we have. Spending it wisely can help us reach our goals, build strong relationships, and create moments we will remember forever. Use it wisely, and it will reward you in many ways.",
    "Technology is changing quickly, making life more connected and convenient. From mobile phones to artificial intelligence, it affects how we work, learn, and live every day. Understanding it can help us stay prepared for the future.",
    "A good book can take you to places you’ve never been and teach lessons you’ve never learned. Reading improves focus, builds imagination, and makes you smarter. It’s a simple habit that can transform your life for the better.",
    "Good friends are like stars. Even when you can’t see them, you know they’re always there. They support you when times are hard and celebrate with you when things go well. True friends make life more meaningful and rewarding.",
    "A quiet morning is the best time to plan your day. It gives you space to think clearly, set priorities, and find motivation. Spending a few moments with yourself can create a sense of calm and direction for the rest of the day."
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

# results
if random_sentence == user_input:
    print("Congratulations! You passed...")
    print(f"Total time taken: {total_time:.2f} seconds")
    print(f"Total words typed: {total_words}")
    print(f"Your typing speed is {wpm:.2f} words per minute.")
else:
    print("You failed ! Try again....")

#end of the program