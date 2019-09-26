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

