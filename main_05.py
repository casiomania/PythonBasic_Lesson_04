# Lesson 04 / Additional task 01
# Additionally:
# There is some text. Implement the following functionality:
# Change the text so that each sentence starts with a capital letter;
# Count the number of times numbers appear in the text;
# Count the number of times punctuation appears in the text;
# Count the number of exclamation points in the text.

some_text = "lorem ipsum is simply dummy text of the printing and typesetting industry. lorem ipsum has been the \nindustry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book!"

sentences = some_text.split('. ')

capitalized_sentences = [sentence.strip().capitalize() for sentence in sentences if sentence.strip()]

capitalized_text = '. '.join(capitalized_sentences)

digits_count = sum(char.isdigit() for char in some_text)

punctuation_count = sum(char in ",.?!:;" for char in some_text)

exclamation_count = some_text.count("!")

print(f"Processed Text:\n{capitalized_text}")
print(f"\nDigits Count: {digits_count}")
print(f"Punctuation Count: {punctuation_count}")
print(f"Exclamation Count: {exclamation_count}")
