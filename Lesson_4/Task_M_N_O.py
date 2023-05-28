# M - Похожа на задачу L 
n = int(input())
m = int(input())
temp = 1
for i in range(1, n + 1):
    for j in range(m):
        if n * m < 10:
            print("{:1}".format(temp), end=" ")
        elif n * m > 10 and n * m < 100:
            print("{:2}".format(temp), end=" ")
        else:
            print("{:3}".format(temp), end=" ")
        temp += n
    temp = 1 + i
    print()

# N - Змейка
n = int(input())
m = int(input())
temp = 1
for i in range(1, n + 1):
    for j in range(m):
        if i % 2 == 1:
            if n * m < 10:
                print("{:1}".format(temp), end=" ")
            elif n * m > 10 and n * m < 100:
                print("{:2}".format(temp), end=" ")
            else:
                print("{:3}".format(temp), end=" ")
            if j < m - 1:
                temp += 1
        elif i % 2 == 0:
            if n * m < 10:
                print("{:1}".format(temp), end=" ")
            elif n * m > 10 and n * m < 100:
                print("{:2}".format(temp), end=" ")
            else:
                print("{:3}".format(temp), end=" ")
            if j < m - 1:
                temp -= 1
    temp += m
    print()    

# O - Змейка 2.0    
n = int(input())
m = int(input())
temp = 1
step2 = 0
step = n * 2 - 1
for i in range(1, n + 1):
    for j in range(1, m + 1): 
        if j % 2 == 1:
            if j < m + 1:
                if n * m < 10:
                    print("{:1}".format(temp), end=" ")
                elif n * m > 10 and n * m < 100:
                    print("{:2}".format(temp), end=" ")
                else:
                    print("{:3}".format(temp), end=" ")
                temp += step
        else:
            if j < m + 1:
                if n * m < 10:
                    print("{:1}".format(temp), end=" ")
                elif n * m > 10 and n * m < 100:
                    print("{:2}".format(temp), end=" ")
                else:
                    print("{:3}".format(temp), end=" ")
                temp += i + step2
    temp = 1 + i
    step = step - 2
    step2 += 1
    print()