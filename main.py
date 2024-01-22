''' Консольний бот помічник '''

def input_error(func):
    ''' Декоратор '''
    def inner(*args):
        try:
            return func(*args)
        except (IndexError, KeyError, ValueError):
            pass
    return inner


def main():
    ''' Функція обробки введення виведення '''
    phone_book = {}
    while True:
        comand = input('Input you comand: ')
        comand_list = comand.lower().split()
        result = handler(comand)(comand_list, phone_book)
        print(result)
        if result == "Good bye!":
            break


@input_error
def handler(comand):
    ''' Функція обробки введених данних '''
    comand_list = comand.lower().split()
    if comand == '':
        return lambda *_: 'Correct you input!'
    if len(comand_list) == 2:
        if comand_list[0] == 'good' and comand_list[1] == 'bye' or\
           comand_list[0] == 'show' and comand_list[1] == 'all':
            return OPERATIONS[comand]
    if comand_list[0] in OPERATIONS:
        return OPERATIONS[comand_list[0]]
    return lambda *_: 'Correct you input!'

@input_error
def handler_hello(*_):
    return 'How can I help you?'

@input_error
def handler_add(comand, phone_book):
    phone_book.update({comand[1]: comand[2]})

@input_error
def handler_change(comand, phone_book):
    phone_book.update({comand[1]: comand[2]})

@input_error
def handler_phone(comand, phone_book):
    return phone_book[comand[1]]

@input_error
def handler_show(_, phone_book):
    return phone_book

@input_error
def handler_exit(*_):
    return "Good bye!"



OPERATIONS = {
    'hello': handler_hello, 'add': handler_add, 'change': handler_change, 'phone': handler_phone,
    'show all': handler_show, 'good bye': handler_exit, 'close': handler_exit, 'exit': handler_exit,
}


main()
