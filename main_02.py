# Lesson 4 / Homework 2
# The user enters a string and a character to search.
# Count the number of times the desired character appears in the string. Print the resulting number on the screen.

try:
    entered_string, search_char = input("Enter a string: "), input("Enter a character to search: ")

    if len(search_char) != 1:
        raise ValueError("Please enter only one character for search.")

    count = 0
    for char in entered_string:
        if char == search_char:
            count += 1

    print(f"The character '{search_char}' appears {count} times in the entered string.")

except ValueError as error:
    print("Error:", error)

except Exception as error:
    print("An error occurred:", error)

