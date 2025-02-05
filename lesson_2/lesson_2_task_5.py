month = int(input())
s = ''

def month_to_season(n):
    if n == 1 or n == 2 or n == 12:
        s = 'Winter'
    elif  3 <= n <= 5:
        s = 'Spring'
    elif 6 <= n <= 8:
        s = 'Summer'
    elif 9 <= n <= 11:
        s = 'Autumn'
    elif n <=0 or n >= 13:
        s = 'Enter correct month'
    return(s)

season = month_to_season(month)
print(season)