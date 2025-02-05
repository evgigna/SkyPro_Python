x, y = int(input('Величина вклада:')), int(input('Количество лет:'))
sum = 0             
rate = 0.1          # % ставка


def bank(x, y):
    for i in range(1, y + 1):
        sum =  x + x * rate
        x = sum
    return sum

sum = bank(x, y)
print('Величина вклада через', y, 'лет составит', round(sum, 2))