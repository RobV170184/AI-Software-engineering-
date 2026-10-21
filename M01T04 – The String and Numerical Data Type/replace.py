# Task 1: replace.py
# String manipulation with replace(), upper(), and reversal

# Save the sentence with exclamation marks
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Replace all exclamation marks with spaces
sentence_with_spaces = sentence.replace("!", " ")
print(sentence_with_spaces)

# Convert the sentence to uppercase
sentence_uppercase = sentence_with_spaces.upper()
print(sentence_uppercase)

# Print the sentence in reverse using slicing
sentence_reversed = sentence_uppercase[::-1]
print(sentence_reversed)
