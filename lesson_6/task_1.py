# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

# 'python task_1.py 28.02.2021'

import sys

MONTH_30_DAYS = [4, 6, 9, 11]


def analyze_date(date_in):

    day, month, year = map(int, date_in.split('.'))

    if day < 1 or day > 31 or month < 1 or month > 12 or year < 1 or year > 9999:
        return False

    elif month in MONTH_30_DAYS and day > 30:
        return False
    
    elif month == 2 and (not is_leap_year(year) and day > 28 or is_leap_year(year) and day > 29):
        return False

    else:
        return True
    
    
def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    
    
def input_command_line():
    day, month, year = [int(i) for i in (sys.argv[1].split('.'))]
    return day, month, year
    
    
if __name__ == '__main__':
    date = input_command_line()
    date = [str(i) for i in date]
    print(analyze_date('.'.join(date)))
    