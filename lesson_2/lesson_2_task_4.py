n = int(input('Введите число:'))

def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        a = 'FizzBuzz'
    elif n % 3 == 0:
        a = 'Fizz'
    elif n % 5 == 0:
        a = 'Buzz'
    else:
        a = n
    return(a)

for j in range(1, n + 1):
    a = fizz_buzz(j)
    print(a)



