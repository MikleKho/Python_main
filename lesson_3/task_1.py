# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов. 

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 3, 5, 7, 9, 0, 0, 0]
temp_set = set(input_list)
result_list = []
for val_temp in temp_set:
    count = 0
    for val_input in input_list:
        count = count + 1 if val_temp == val_input else count
        if count == 2:
            result_list.append(val_temp)
            break
print(f'Исходный список: {input_list}')
print(f'Список повторений: {result_list}')
