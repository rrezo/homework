# Symbol remover - removes a given symbol or symbols from a sentence

sentence = 'Hello! My name is John! MY NAME IS JOHN!!!'
symbol = '!'

def symbol_remover(sentence, symbol):
    new_sentence = ''
    for char in sentence:
        if char != symbol:
            new_sentence += char
    return new_sentence

print(symbol_remover(sentence, symbol))


# Name finder - check if the name exists in the list, its index and creates
# a new list if the index is ODD. If the index is even prints "It's all good"

names = ['John', 'Kate', 'Dave', 'Den', 'Adele']
name = 'Kate'

def name_finder(names, name):
    if name not in names:
        return 'Not found'
    else:
        if names.index(name) % 2 == 0:
            return "It's all good"
        else:
            names.remove(name)
            return names

print(name_finder(names, name))

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


int_list = []
number = 0

# Square number generator

for i in range(0, 100):
    i = (i + 1)**2
    int_list.append(i)

print(int_list)


# Cars list creator

cars_list = []

while True:
    car_name = input('Input a car name (or press q to quit): ')
    if car_name == 'q':
        break
    cars_list.append(car_name)

print('Your list is: ' + str(cars_list))




