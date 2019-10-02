# Get person's cars count

people = [
    {
        'name': 'Steve',
        'country': 'Ukraine',
        'cars': ['BMW', 'Renault']
    },
    {
        'name': 'John',
        'country': 'Poland',
        'cars': ['Opel']
    },
    {
        'name': 'Peter',
        'country': 'USA',
        'cars': ['Ford', 'Nissan', 'Audi']
    }
]

people_new = {name.get('name'): len(name.get('cars')) for name in people}

print(people_new)

# Task1. Write a function using list comprehensions that takes a list of
# strings and removes those that contain 4 characters or less


def remove_shorts(strings: list) -> list:
    return [name for name in strings if len(name) > 4]


assert remove_shorts(['telegram', 'sport', 'call', 'football', 'jet']) \
       == ['telegram', 'sport', 'football']
assert remove_shorts(['zombie', 'vision', 'cat', 'ring', 'telescope']) \
       == ['zombie', 'vision', 'telescope']

print(remove_shorts(['telegram', 'sport', 'call', 'football', 'jet']))
print(remove_shorts(['zombie', 'vision', 'cat', 'ring', 'telescope']))

# Task2. Write a function using list comprehensions that takes a string
# and changes letter's case from upper to lower and vice versa


def change_case(string: str) -> str:
    return ''.join([ch.lower() if ch.isupper() else ch.upper() for ch in string])


assert change_case("HELLO") == "hello"
assert change_case("Hi! I'm Jim :)") == "hI! i'M jIM :)"
assert change_case("welcome y'all") == "WELCOME Y'ALL"

print(change_case("HELLO"))
print(change_case("welcome y'all"))


# Task3. Write a function using dict comprehensions that takes a list of
# strings and outputs a dictionary where keys are strings and values
# are booleans that say whether the word is a palindrome or not


def detect_palindromes(strings: list) -> dict:
    return {name: name[::] == name[::-1] for name in strings}


assert detect_palindromes(['madam', 'joy', 'fish']) == {
    'madam': True,
    'joy': False,
    'fish': False
}

assert detect_palindromes(['print', 'mom', 'dad']) == {
    'print': False,
    'mom': True,
    'dad': True
}

print(detect_palindromes(['madam', 'joy', 'fish']))
print(detect_palindromes(['print', 'mom', 'dad']))


# Task4. Write a function that takes 2 dictionaries where keys
# are cars and values are their prices. The function checks whether
# the sum of prices in 1 dictionary is equal to the sum in the 2nd


def compare_prices(cars1: dict, cars2: dict) -> bool:
    return sum(cars1.values()) == sum(cars2.values())


assert compare_prices({'BMW': 20000, 'Nissan': 15000},
                      {'Mustang': 30000, 'Renault': 5000}) is True
assert compare_prices({'Volvo': 13000, 'Infinity': 80000},
                      {'Ford GT': 100000, 'Lada': 3000}) is False


print(compare_prices({'BMW': 20000, 'Nissan': 15000},
      {'Mustang': 30000, 'Renault': 5000}))
print(compare_prices({'Volvo': 13000, 'Infinity': 80000},
                      {'Ford GT': 100000, 'Lada': 3000}))