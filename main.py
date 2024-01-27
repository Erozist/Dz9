''' Консольний бот помічник '''

def input_error(func):
    ''' Декоратор '''
    def inner(*args):
        try:
            return func(*args)
        except (IndexError, KeyError, ValueError):
            return 'Name or Number not correct!'
    return inner


def main():
    ''' Функція обробки введення виведення '''
    phone_book = {}
    while True:
        comand_list = input('Input you comand: ')
        comand = comand_list.lower().split()
        result = handler(comand_list)(comand, phone_book)
        print(result)
        if result == "Good bye!":
            break


@input_error
def handler(comand_list):
    ''' Функція обробки введених данних '''
    comand = comand_list.lower().split()
    if comand_list == '':
        return lambda *_: 'Correct the input!!! The entered command is empty!!!'
    if len(comand) > 3:
        return lambda *_: 'You comand is very long'
    if len(comand) == 2:
        if comand[0] == 'good' and comand[1] == 'bye' or\
           comand[0] == 'show' and comand[1] == 'all':
            return OPERATIONS[comand_list]
    if comand[0] in OPERATIONS:
        return OPERATIONS[comand[0]]
    return lambda *_: f'Correct the input!!! The entered command <{comand}> is not valid!!!'

@input_error
def handler_hello(*_):
    return 'How can I help you?'

@input_error
def handler_add(comand, phone_book):
    print(comand[1], comand[2])
    if comand[1] in phone_book:
        return f'<{comand[1]}> is already a contact.'
    phone_book.update({comand[1]: comand[2]})
    return f'A new contact {comand[1]} has been created.'

@input_error
def handler_change(comand, phone_book):
    if comand[1] in phone_book:
        phone_book[comand[1]] = [comand[2]]
        return f'A new number has been recorded {comand[2]}.'
    return f"The contact {[comand[1]]} is not in the phone book."

@input_error
def handler_phone(comand, phone_book):
    if comand[1] in phone_book:
        return f"The contact {[comand[1]]} phone number {phone_book[comand[1]]}."
    return f"The contact {[comand[1]]} is not in the phone book."

@input_error
def handler_show(_, phone_book):
    return f'Oll list of telephone book: {phone_book}'

@input_error
def handler_exit(*_):
    return "Good bye!"



OPERATIONS = {
    'hello': handler_hello, 'add': handler_add, 'change': handler_change, 'phone': handler_phone,
    'show all': handler_show, 'good bye': handler_exit, 'close': handler_exit, 'exit': handler_exit,
}


main()
