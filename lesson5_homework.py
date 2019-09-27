# Symbol remover - removes a given symbol or symbols from a sentence

sentence = 'Hello! My name is John! MY NAME IS JOHN!!!'
symbol = '!'

def symbol_remover(sentence, symbol):
    new_sentence = ''
    for char in sentence:
        if char == symbol:
            continue
        new_sentence += char
    return(new_sentence)

print(symbol_remover(sentence, symbol))


# Name finder - check if the name exists in the list, its index and creates
# a new list if the index is ODD. If the index is even prints "It's all good"

names = ['John', 'Kate', 'Dave', 'Den', 'Adele']
name = 'Kate'

def name_finder(names, name):
    if name not in names:
        print('Not found')
    else:
        if names.index(name) % 2 == 0:
            print("It's all good")
        else:
            names.remove(name)
            print(names)

name_finder(names, name)

# Lis sum checker - removes numbers from the list until sum < 200

nums = [75, 81, 96, 213, 94, 15, 38, 11]

while sum(nums) > 200:
    nums.pop()

print(nums)

# Collatz sequence

num = 3

while num != 1:
    if num % 2 == 0:
        num = num / 2
        print(num)
    else:
        num = (num * 3) + 1
        print(num)

