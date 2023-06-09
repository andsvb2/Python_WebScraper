import string

vowels = ['a', 'e', 'i', 'o', 'u']

text = input()

for letter in text:
    if letter not in string.ascii_letters:
        break
    if letter.lower() in vowels:
        print('vowel')
    else:
        print('consonant')
