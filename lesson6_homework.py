# Insert whitespace - inserts spaces in text between lowercase and
# uppercase letters.


def insert_whitespace(text):
    new_text = ''
    for char in text:
        if char.isupper():
            new_text += ' ' + char
        else:
            new_text += char

    return new_text.lstrip()


print(insert_whitespace('SheWalksToTheBeach'))


# Calculator without using if


def calculator(num1, num2, operation):
    operations = {
        'sum': num1 + num2,
        'mul': num1 * num2,
        'div': num1 / num2,
        'ded': num1 - num2
    }
    return operations[operation]


print(calculator(2, 5, 'mul'))


# Wrap - breaks a string by a given number of symbols


def wrap(string, width):
    new_list = list(string)
    new_list1 = []
    for i in range(0, len(new_list), width):
        chunk = new_list[i:i + width] + list('\n')
        new_list1 += chunk

    return ''.join(new_list1)


print(wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4))

# Оператор else в цикле for выполняется только в том случае, если выход
# из условия if не был произведен при помощи команды break.

# Custom split

def custom_split(string, delimiter):
    new_list = []
    new_string = ''
    for ch in string:
        if ch != delimiter:
            new_string += ch
        else:
            new_list.append(new_string)
            new_string = ''

    return new_list


print(custom_split('We live inside a dream', ' '))