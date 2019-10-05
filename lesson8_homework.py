# Write a custom sum function that takes any number of arguments and returns
# their sum. If the number of arguments is more than 20, return None instead


def custom_sum(*args) -> int:
    if len(args) < 20:
        return sum(args)


assert custom_sum(12, 12, 13) == 37
assert custom_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                  11, 12, 13, 14, 15, 16, 17, 18, 19, 20) is None

print(custom_sum(12, 12, 13))
print(custom_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                  11, 12, 13, 14, 15, 16, 17, 18, 19, 20) is None)


# Write a function that takes a list of strings and removes those strings
# that don't consist of unique letters

def remove_string_doubles(strings: list) -> list:
    return [name for name in strings if len(name) == len(set(name))]


assert remove_string_doubles(['cat', 'escape', 'template', 'head']) == \
       ['cat', 'head']
assert remove_string_doubles(['lamp', 'hash']) == ['lamp']


print(remove_string_doubles(['cat', 'escape', 'template', 'head']))
print(remove_string_doubles(['lamp', 'hash']))


# Write a function that takes a sentence (string) and any number of
# key-word arguments. All kwargs are filters for that question.
# These filters decide whether the function returns True or False
# Possible filters:
#   - max_length: integer !REQUIRED FILTER
#   - includes: list of strings (substring that the sentence must contain)
#   - has_spaces: boolean
#   etc
#
# max_length is required kwarg. If it hasn't been provided, the function
# must return None
#
# see asserts for better understanding


def is_valid(string, **filters):
    pass


# assert is_valid('Hi! My name is Jim', max_length=30, has_spaces=True) is True
# assert is_valid('RobertSteveJohn', max_length=10, has_spaces=False) is False
# assert is_valid('Hey guys! Have you ever played football:)',
#                 includes=['?', '.'], max_length=100) is False
# assert is_valid("What's up?", has_spaces=True) is None