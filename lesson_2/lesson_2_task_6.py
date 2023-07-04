lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
l = len(lst)

#for i in range(0, l):
#    if lst[i] < 30 and lst[i] % 3 == 0:
#        print(lst[i], end = ' ')

result = [x for x in lst if x < 30 and x % 3 == 0]  
print(result)