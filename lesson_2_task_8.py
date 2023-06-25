# Задание 8. Range

# Изучите статью: https://pythonchik.ru/osnovy/python-range.
# Создайте список [ 18, 14, 10, 6, 2 ] с помощью функции range() и выведите его на экран.

list = [ 18, 14, 10, 6, 2 ]
l = len(list)

for i in range(0, l):
    print(list[i], end = ' ')