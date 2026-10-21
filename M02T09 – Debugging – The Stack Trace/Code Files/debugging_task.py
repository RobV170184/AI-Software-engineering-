# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])  # Bug fix 1: changed 'k' to 'key' (k was undefined; the loop variable is named 'key')

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!",
                         "bart": "Eat My Shorts!",
                         "marge": "Mmm~mmmmm",
                         "homer": "d'oh!",  # Bug fix 2: changed single quotes to double quotes so the apostrophe in d'oh! doesn't break the string
                         "maggie": "(Pacifier Suck)"
                         }

print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])  # Bug fix 3: wrapped keys in a list [] so they are passed as a single iterable argument

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''
