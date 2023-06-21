# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку. 

string_in = 'At runtime, "Python" will try to look for common patterns and type stability in the executing code. Python will then replace the current operation with a more specialized one. This specialized operation uses fast paths available only to those use cases/types, which generally outperform their generic counterparts. This also brings in another concept called inline caching, where Python caches the results of expensive operations directly in the bytecode.'
SYMBOLS_TABLE = {ord('.') : None, ord(',') : None, ord('"') : None, ord(':') : None}
string_temp_list = string_in.translate(SYMBOLS_TABLE).lower().split()
print('------------------')
print(f'Строка: {string_in}')
print('------------------')
string_temp_set = set(string_temp_list)
result_list = [(value, string_temp_list.count(value)) for value in string_temp_set]
result_list.sort(key = lambda i: i[1], reverse = True)
print(f'Список частых повторений слов: {result_list[0:10:1]}')
print('------------------')
