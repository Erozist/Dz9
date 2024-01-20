''' Консольний бот помічник '''

def input_error(func):
    ''' Декоратор '''
    def inner():
        try:
            func()
        except (IndexError, KeyError, ValueError):
            print('Try again!')
            func()
    return inner


@input_error
def main():
    ''' Функція обробки введення виведення '''
    phone_book = {}
    while True:
        comand = input('Input you comand: ')
        comand = comand.lower().split()
        result = handler(comand, phone_book)
        print(result)
        if result == "Good bye!":
            break


def handler(comand, phone_book):
    ''' Функція обробки введених данних '''
    if comand[0] == 'hello':
        result = 'How can I help you?'
    if (comand[0] == "good" and comand[1] == "bye")\
        or comand[0] == "close" or comand[0] == "exit":
        result = "Good bye!"
    if comand[0] == 'add':
        result = phone_book.update({comand[1]: comand[2]})
    if comand[0] == 'change':
        result = phone_book.update({comand[1]: comand[2]})
    if comand[0] == 'phone':
        result = phone_book[1]
    if comand[0] == 'show' and comand[1] == 'oll':
        result = phone_book.items()
    return result

main()
