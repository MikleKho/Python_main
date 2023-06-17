# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint

if __name__ == '__main__':
    number = randint(0, 1000)
    for i in range(1, 11):
        number_in = int(input(f"Попытка {i}. Введите число: "))
        if number_in == number:
            print(f"Вы угадали, число {number}")
            sys.exit()
        print("Загаданное число больше") if number > number_in else print("Загаданное число меньше")
    print("Попытки закончились")
 
