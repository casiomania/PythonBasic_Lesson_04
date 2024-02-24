# Lesson 4 / Homework 1
# The user enters a string from the keyboard.
# Count the number of letters and digits in the string. Display both numbers on the screen (use a loop).

try:
    entered_string = input("Enter string: ")
    letters = 0
    digits = 0

    for char in entered_string:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1

    qty = [("Letters", letters), ("Digits", digits)]

    for i in range(len(qty)):
        print(f"{qty[i][0]} count: {qty[i][1]}")

except Exception as error:
    print(f"Error: {error}")
