possible_palindrome = input()

def palindrome_check(word: str):
    reversed_word = word[::-1]

    if reversed_word == word:
        print("Palindrome")
    else:
        print("Not palindrome")

palindrome_check(possible_palindrome)