# String remover - removes string by its index

test = 'test1, test2, test3, test4, test5'

#Ver1 - by using a .replace method

def var_replacer(string, index):
    new_list = string.split(', ')
    if not string.endswith(str(index)):
        remove_word = f'{new_list[index - 1]}, '
        new_text = string.replace(remove_word, '')
        return new_text
    else:
        remove_word = f', {new_list[index - 1]}'
        new_text = string.replace(remove_word, '')
        return new_text

print(var_replacer(test, 5))

# Ver2 - without using a .replace method

def var_remover(string, index):
    new_list = string.split(', ')
    if index == 0:                            #avoid deleting index -1
        return 'Choose index from 1 to 5'
    new_list.pop(index - 1)
    new_str = ', '.join(new_list)
    return new_str

print(var_remover(test, 5))



# Domain extractor - finds a domain in the string and prints it out

def domain_ext(string):
    domain_name = string.split('//')[-1].split('www.')[-1].split('/')[0]
    return domain_name

print(domain_ext('https://www.google.com/doodles/'))
print(domain_ext('https://realpython.com/courses/python-thonny/'))



# Random number - returns True if user guesses the random number

import random
def random_number(user_number):
    number = random.randint(0, 10)
    print(number)
    return (number is int(user_number))

print(random_number(1))
