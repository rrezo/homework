from functools import wraps


# ------------------------------------------------------Without wraps, Ver1

# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
# For example:
#   "add called with 4, 5"


def logger(func):
    def wrapper(*args):
        return f"{func.__name__} called with {args}"
    return wrapper


@logger
def add(x, y):
    return x + y


print(add(4, 5))

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

print(square_all(1, 2, 3, 4, 5))
print(square_all.__name__)


# Write a decorator that takes a list of stop words and replaces in them
# with * inside decorated function


def stop_words(words: list):
    def decorator (func):
        def wrapper(args):
            new_string = func(args)
            for word in words:
                new_string = new_string.replace(word, '*')
            return new_string
        return wrapper
    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("\n\nSteve"))
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
print(create_slogan.__name__)
print('\n\n')

# Write a decorator arg_rules that validates arguments passed to the function
# A decorator should take 3 arguments:
#   max_length: 15
#   type_: str
#   contains: []  - list of symbols that an argument should contain
#
# If some of the rules' checks returns False, the function should return False
# and print the reason it failed
#
# Otherwise return result


def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(args):
            if type(args) == type_ and len(args) < max_length \
                    and all(word in args for word in contains):
                return func(args)
            return False
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('S@SH05'))
print(create_slogan('0@cde'))
print(create_slogan.__name__)
assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

# ------------------------------------------------------With wraps, Ver2


# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
# For example:
#   "add called with 4, 5"


def logger(func):
    @wraps(func)
    def wrapper(*args):
        return f"{func.__name__} called with {args}"
    return wrapper


@logger
def add(x, y):
    return x + y


print(add(4, 5))

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

print(square_all(1, 2, 3, 4, 5))
print(f"Function name: -> {square_all.__name__}")


# Write a decorator that takes a list of stop words and replaces in them
# with * inside decorated function


def stop_words(words: list):
    def decorator (func):
        @wraps(func)
        def wrapper(args):
            new_string = func(args)
            for word in words:
                new_string = new_string.replace(word, '*')
            return new_string
        return wrapper
    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("\n\nSteve"))
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
print(f"Function name: -> {create_slogan.__name__}\n\n")

# Write a decorator arg_rules that validates arguments passed to the function
# A decorator should take 3 arguments:
#   max_length: 15
#   type_: str
#   contains: []  - list of symbols that an argument should contain
#
# If some of the rules' checks returns False, the function should return False
# and print the reason it failed
#
# Otherwise return result


def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        @wraps(func)
        def wrapper(args):
            if type(args) == type_ and len(args) < max_length \
                    and all(word in args for word in contains):
                return func(args)
            return False
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('S@SH05'))
print(create_slogan('0@cde'))
print(f"Function name: -> {create_slogan.__name__}")
assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'