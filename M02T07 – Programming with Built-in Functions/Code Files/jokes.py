# M02T07: Built-in Functions - Random joke generator
# This program displays a random joke using the random module

import random

# Create a list of jokes with their punchlines
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you call a fake noodle? An impasta!",
    "Why don't eggs tell jokes? They'd crack each other up!",
    "What did the ocean say to the beach? Nothing, it just waved!"
]

# Display a random joke
random_joke = random.choice(jokes)
print(random_joke)
