# Task 2: manipulation.py
# Interactive string manipulation program

# Get a sentence from the user
sentence = input("Enter a sentence: ")

# Calculate and display the length of the sentence
length = len(sentence)
print(f"Length of the sentence: {length}")

# Find the last letter of the sentence
last_letter = sentence[-1]

# Replace every occurrence of the last letter with '@'
sentence_replaced = sentence.replace(last_letter, "@")
print(f"Sentence with last letter replaced by '@': {sentence_replaced}")

# Print the last 3 characters backwards
last_three_backwards = sentence[-3:][::-1]
print(f"Last 3 characters backwards: {last_three_backwards}")

# Create a five-letter word using the first 3 and last 2 characters
five_letter_word = sentence[:3] + sentence[-2:]
print(f"Five-letter word: {five_letter_word}")
