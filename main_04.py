# Lesson 04 / Homework 04
# Given a string.
# - First print the third character of this string.
# - In the second line print the penultimate character of this string.
# - In the third line print the first five characters of the string.
# - In the fourth line print the entire string except the last two characters.
# - In the fifth line print all characters with even indices (assuming that indexing starts from 0,
#   so the characters are printed from the first).
# - In the sixth line print all the characters with odd indexes, that is,
#   starting from the second character of the line.
# - In the seventh line print all the characters in reverse order.
# - In the eighth line print all the characters in the string in reverse order, starting with the last one.
# - In the ninth line print the length of the string.

try:
    text = input("Enter string: ")

    print(text[2])
    print(text[-2])
    print(text[:5])
    print(text[:-2])
    print(text[::2])
    print(text[1::2])
    print(text[::-1])
    print(text[::-2])
    print(len(text))

except Exception as error:
    print("Error:", error)
