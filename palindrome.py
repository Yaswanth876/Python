def is_palindrome(word):
    return word == word[::-1]

str_input = input("Enter a word: ")
if is_palindrome(str_input.lower()):
    print("It is a palindrome!")
else:
    print("It's not a palindrome!")