# a.
cub_num = []
for i in range(1, 1000):
    a = i ** 3
    cub_num.append(a)
num_7 = []
for i in cub_num:
    n = i
    n1 = n % 10
    n2 = n % 100 // 10
    n3 = n % 1000 // 100
    n4 = n % 10000 // 1000
    n5 = n % 100000 // 10000
    n6 = n % 1000000 // 100000
    n7 = n % 10000000 // 1000000
    n8 = n % 100000000 // 10000000
    n9 = n % 1000000000 // 100000000
    n10 = n % 1000000000 // 10000000000
    sum_num = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
    t = sum_num / 7
    if t == int(t):
        num_7.append(i)

print(num_7)

# b.
s = '.' # Точка для проверки
for i in num_7:
    n = i + 17
    n1 = n % 10
    n2 = n % 100 // 10
    n3 = n % 1000 // 100
    n4 = n % 10000 // 1000
    n5 = n % 100000 // 10000
    n6 = n % 1000000 // 100000
    n7 = n % 10000000 // 1000000
    n8 = n % 100000000 // 10000000
    n9 = n % 1000000000 // 100000000
    n10 = n % 1000000000 // 10000000000
    sum_num = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
    t = sum_num / 7
    if t == int(t):
        s += str(i) + '.'

print(s)




