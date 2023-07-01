# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различные случайные варианты и выведите 4 успешных расстановки. *Выведите все успешные варианты расстановок

from itertools import permutations


def chek_chess_queens(x_list, y_list, size=8):
    
    for i in range(size):
        for j in range(i + 1, size):
            # print(i, j)
            if x_list[i] == x_list[j] or y_list[i] == y_list[j] or abs(x_list[i] - x_list[j]) == abs(y_list[i] - y_list[j]):
                return False
    return True

    
if __name__ == '__main__':
    x_list = [1, 2, 3, 4, 5, 6, 7, 8]
    y_list = [8, 2, 4, 1, 7, 5, 3, 6]
    print(chek_chess_queens(x_list, y_list))

    x_list = [1, 2, 3, 4, 5, 6, 7, 8]
    count = 0
    for y_list in permutations([1, 2, 3, 4, 5, 6, 7, 8], 8):
        if chek_chess_queens(x_list, y_list):
            print('\n', x_list, '\n', list(y_list), '\n -------------------\n')
            count = count + 1 
    print(f'Всего найдено {count} комбинации')
