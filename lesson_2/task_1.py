# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.


def rebase_number(number_in, base):
    BASE_SYMBOLS = ['0', '1', '2', '3', '4','5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    number_str_out = []
    while number_in != 0:
        number_str_out.append(BASE_SYMBOLS[number_in % base])
        number_in //= base
    number_str_out.reverse()
    return ''.join(number_str_out)


if __name__ == '__main__':
    base = 16
    number_in = int(input('Ведите целое десятичное число для преобразования: '))
    print(f'Результат преобразования: {rebase_number(number_in, base)}')
    print(f'Проверка: {hex(number_in)}')

