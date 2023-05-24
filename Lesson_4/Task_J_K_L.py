# J - Таблица вариантов разделения апельсина.
number = int(input())
print("А Б В")
for i in range(1, number):
    for j in range(1, number):
        for k in range(1, number):
            if number - (i + j + k) == 0:
                print(i, j, k)

# K - Требуется вывести общее количество простых чисел среди введённых (кроме N).
number = int(input())
counter = 0


def is_prime(temp):
    if temp < 2:
        return False
    for i in range(2, int(temp ** 0.5 + 1)):
        if temp % i == 0:
            return False
    else:
        return True


for i in range(number):
    temp = int(input())
    if is_prime(temp) is True:
        counter += 1
print(counter)                

# L - Нужно вывести сформированный числовой прямоугольник требуемого размера в красивом виде.
n = int(input())
m = int(input())
temp = 1
for i in range(n):
    for j in range(m):
        if n * m < 10:
            print("{:1}".format(temp), end=" ")
        elif n * m > 10 and n * m < 100:
            print("{:2}".format(temp), end=" ")
        else:
            print("{:3}".format(temp), end=" ")
        temp += 1
    print()
