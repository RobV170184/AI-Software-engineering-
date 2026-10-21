# M02T04: String Handling 

# Get input from user
user_string = input("Enter a string: ")

# Part 1: Alternate characters uppecase and lowercase
result_chars = ""
for index in range(len(user_string)):
    if index % 2 == 0:
        result_chars += user_string[index].lower()
    else:
        result_chars += user_string[index].upper()

print("Alternate characters:", result_chars)

# Part 2: Alternatewords lowercase and uppercase
words = user_string.split()
result_words = []

for index in range(len(words)):
 if index % 2 == 0:
    result_words.append(words[index].lower())
else:
    result_words.append(words[index].upper())

result_string = " ".join(result_words)
print("Alternate words:", result_string)
