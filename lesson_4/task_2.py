# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.


def reverse_dict(**kwargs):

    dict_reverse = {value: key for key, value in kwargs.items()}
    return dict_reverse


dict_out = reverse_dict(first_symbol = 'A', second_symbol = 'B', third_symbol = 'C')
print(dict_out)