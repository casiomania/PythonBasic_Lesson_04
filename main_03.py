# Lesson 4 / Homework 3
# The user enters a string, a word to search for, and a word to replace from the keyboard.
# Replace one word in the string with another. The resulting string is displayed on the screen.

try:
    entered_string = input("Enter a string: ")
    search_word = input("Enter a word to search: ")
    replace_word = input("Enter a word to replace: ")

    modified_string = entered_string.replace(search_word, replace_word)

    if modified_string == entered_string:
        raise ValueError(f"The word '{search_word}' is not found in the entered string.")

    print("Resulting string:", modified_string)

except ValueError as error:
    print("Error:", error)

except Exception as error:
    print("An error occurred:", error)
