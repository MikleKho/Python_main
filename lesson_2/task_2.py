# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

import fractions
import sys


def do_fraction_min(fr):
    if fr[0] == 0:
        fr = []
        return fr
    elif fr[0] == fr[1]:
        fr = [1]
        return fr
    div_limit = int(min(fr)**0.5) + 2
    start_divider = 2
    flag_div = True
    while flag_div:
        flag_div = False
        for i in range(start_divider, div_limit):
            if fr[0] % i == 0 and fr[1] % i == 0:
                fr[0] = int(fr[0] / i)
                fr[1] = int(fr[1] / i)
                flag_div = True
                start_divider = i
    if fr[0] > fr[1]:
            fr.append(fr[0] // fr[1])
            fr[0] = fr[0] % fr[1]
    return fr


if __name__ == '__main__':
    fr_1 = input('Введите первую дробь вида "12/43": ').split('/')
    fr_1 = [int (x) for x in fr_1]
    fr_2 = input('Введите первую дробь вида "12/43": ').split('/')
    fr_2 = [int (x) for x in fr_2]
    if fr_1[1] == 0 or fr_2[1] == 0:
        print('Деление на ноль недопустимо!')
        sys.exit()
    
    print('--------------------------------------------')
    fr_mult = [fr_1[0] * fr_2[0], fr_1[1] * fr_2[1]]
    fr_mult = do_fraction_min(fr_mult)

    fr_sum = [fr_1[0] * fr_2[1] + fr_2[0] * fr_1[1], fr_1[1] * fr_2[1]]
    fr_sum = do_fraction_min(fr_sum)
   
    match len(fr_mult):
        case 0:
            print('Произведение дробей равно: 0')
        case 1:
            print(f'Произведение дробей равно: {fr_mult[0]}')
        case 2:
            print(f'Произведение дробей равно: {fr_mult[0]}/{fr_mult[1]}')
        case 3:
            print(f'Произведение дробей равно: {fr_mult[2]} {fr_mult[0]}/{fr_mult[1]}')
    
    match len(fr_sum):
        case 0:
            print('Сумма дробей равна: 0')
        case 1:
            print(f'Сумма дробей равна: {fr_sum[0]}')
        case 2:
            print(f'Сумма дробей равна: {fr_sum[0]}/{fr_sum[1]}')
        case 3:
            print(f'Сумма дробей равна: {fr_sum[2]} {fr_sum[0]}/{fr_sum[1]}')

    fr_1_check = fractions.Fraction(fr_1[0], fr_1[1])
    fr_2_check = fractions.Fraction(fr_2[0], fr_2[1])
    print(f'Проверочное значение произведения: {fr_1_check * fr_2_check}')
    print(f'Проверочное значение суммы: {fr_1_check + fr_2_check}')
