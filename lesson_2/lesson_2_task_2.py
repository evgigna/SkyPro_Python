x = input('Введите год:')

def is_year_leap(year):
    if year % 4 == 0:
        leap = True
    else:
        leap = False
    return leap

if x.isdigit() == True:
    x = int(x)
    a = is_year_leap(x)
    print('год', x, ':', a)
else:
    print('Введите корректное значение')