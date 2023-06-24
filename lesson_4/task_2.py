# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.


def reverse_dict(**kwargs):

    for key, value in kwargs.items():
        print(f'Key: {key} Value: {value}')

    dict_reverse = {value: key for key, value in kwargs.items()}

    for key, value in dict_reverse.items():
        print(f'Key: {key} Value: {value}')


reverse_dict(first_symbol = 'A', second_symbol = 'B', third_symbol = 'C')