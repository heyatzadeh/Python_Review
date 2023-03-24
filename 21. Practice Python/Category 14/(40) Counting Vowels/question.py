# ----------------- Program Task Description
# Write a program that takes a string input from the user and counts how many times each of the five vowel characters have been repeated in the string and returns the result.

given_sentence = "ali hassan hossein bad good ugly"
vowels = "aeiou"

result = list(filter(lambda x: x in vowels, given_sentence))
print(len(result))
