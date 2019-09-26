names = ['Janie', 'Daniel', 'Steve', 'Bob', 'Rob']

print(len(names))
names.append('David')
print(names[::-1])
names.insert(0, 'Victor')   #add string with a given index
names.remove('Daniel')      #removes first match string
del names[5]                #removes particular index in the list
names.reverse()             #reversed the list
names.sort()                #sorts in alphabet order by default or numbers

print(names)

print('Victor' in names)    #returns True or falls if exists in the list

sentence = 'Hi, my name is Steve'
words = sentence.split(' ')
print(len(words))

sentence2 = 'Hi-my-name-is-Karl'
words2 = sentence2.split('-')
print(words2)

sentence3 = ', '.join(names)    #', ' - is a template how to concatenate
print(sentence3)

print(names.index('Steve'))    #prints string index

name1 = names[1]
name2 = names[3]

print(name1, name2)

name4 = names.pop()             #removes the last str and evaluates to a new
                                #variable (vs .remove)
print(names)
names.append('Karl')
names2 = names
print(names is names2)

print(names)
print(names2)

names3 = names.copy()         #makes a copy of the existing list
print(names3 is names)

#.copy and deepcopy!!!

nm = ['bob', 'rob', 'john']
nm2 = nm.copy()

print(nm2)

# -------------------------------------------TUPLES
names = ['Jane', 'Steve', 'Robert']
print(type(names))

names2 = ('Jane', 'Steve', 'Robert')
print(type(names2))

names3 = list(names2)       #creates a list variable of a tuple

a = 15
b = 34
a, b = b, a                #swaps variables

name = 'Steve'
names = name,              #creating a tuple by using a coma
print(type(names))

Task
f - strings

def tag_add(sentence, tag):
    html = f"<{tag}>{sentence}</{tag}>"
    return html

print(tag_add('word', 'b'))

name = 'Steve'
age = 20

def str_remove(name, age):
    print(f'Hi! my name is {name}, I am {age} years old')
    sentence = f'Hi! my name is {name}, I am {age} years old'
    new_sentence = sentence.replace(name, '')
    return new_sentence

print(str_remove(name, age))

#howemork
def str_reverser(string):
    list1 = list(string)
    list1.reverse()
    return ''.join(list1)

print(str_reverser('Hello world'))

test = 'test1, test2, test3, test4, test5'
# index = int(input())

#no using replace. user types a number what index to remove
#at the end we need to receive a string without elements

def var_remover(list, index):
    new_list = test.split(', ')
    new_list.pop(int(index) - 1)
    new_text = ', '.join(new_list)
    return new_text


print(var_remover(test, 2))






