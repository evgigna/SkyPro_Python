# Задание 6. Фильтрация списка

# Дан список lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20].
# Необходимо вывести элементы, которые одновременно:
#    1. меньше 30,
#    2. делятся на 3 без остатка.

lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
l = len(lst)

for i in range(0, l):
    if lst[i] < 30 and lst[i] % 3 == 0:
        print(lst[i], end = ' ')