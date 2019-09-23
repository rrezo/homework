# Strings checker - checks if the string is < 7 symbols and prints 3
# symbols in the middle
# @Dave: this program works if the string symbols quantity is odd,
# otherwise if it is even it will print 4 symbols (JhonDipPetal->DipP)

def strings_check(string):
    if len(string) < 7 and len(string) % 2 == 0:
        return 'Error'
    elif len(string) % 2 == 0:
        return 'Error'
    else:
        tab = (len(string) - 3)/2
        substring = string[int(tab):int(-tab)]
        return substring

print(strings_check('JhonDipPeta'))



# String words counter - counts quantity of the given word in the string

def string_counter(string, substring):
    #TODO add a condition the word is not a part of the word
        return string.lower().count(substring.lower())

print(string_counter("Hey guys, my name is Jack. "
                     "And my favourite color is green", "My"))



# Integer reverser - returns True if the reversed integer == integer given

def int_reverser(integer):
    str_int = str(integer)
    if str_int == str_int[::-1]:
        return True
    else:
        return False

print(int_reverser(323))



# Symbol remover - removes a string symbol with a given index number

def symbol_rem(string, index):
    return f"{string[:index]}{string[index + 1:]}"

print(symbol_rem('cat', 1))



# Integer checker - checks if on of the words == 10 or their sum == 10

def int_checker(int1, int2):
    if (int1 == 10) or (int2 == 10):
        return True
    elif (int1 + int2) == 10:
        return True
    else:
        return False

print(int_checker(-5, 15))






