# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.


def rebase_number(number_in, base, BASE_SYMBOLS):
    number_str_out = []
    while number_in != 0:
        number_str_out.append(BASE_SYMBOLS[number_in % base])
        number_in //= base
    number_str_out.reverse()
    return ''.join(number_str_out)


if __name__ == '__main__':
    base = 16
    BASE_SYMBOLS = '0123456789ABCDEF'
    number_in = int(input('Ведите целое десятичное число для преобразования: '))
    print(f'Результат преобразования: {rebase_number(number_in, base, BASE_SYMBOLS)}')
    print(f'Проверка: {hex(number_in)}')

