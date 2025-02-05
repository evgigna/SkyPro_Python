import math

a = float(input('Сторона квадрата:'))

def square(a):
    s = a ** 2
    return s

sq = square(a)

print('Площадь квадрата:', math.ceil(sq))