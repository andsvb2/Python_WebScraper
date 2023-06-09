import json

# The following lines create dictionaries from the input. Do not modify them, please
first_family = json.loads(input())
second_family = json.loads(input())

# Work with the 'first_family' and 'second_family' and create a new dictionary
kindred = {}
kindred.update(first_family)
kindred.update(second_family)
print(kindred)
