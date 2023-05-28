# M - Массовое возведение в степень.
# Вводится натуральное число N — количество чисел.
# В каждой из последующих N строк записано по одному числу.
# В последней строке записано натуральное число P — степень, в которую требуется возвести числа.
number = int(input())
list_temp = []
for i in range(1, number + 1):
    temp = int(input())
    list_temp.append(temp)
    if i >= number:
        degree = int(input())
        for num in list_temp:
            print(num ** degree)

# N - Массовое возведение в степень 2.0
number = input().split(" ")
degree = int(input())
for i in range(len(number)):
    print(int(number[i]) ** degree, end=" ")            

# O - НОД 3.0
numbers = input().split(" ")
max_num = 0
for i in range(len(numbers)):
    if int(numbers[i]) > max_num:
        max_num = int(numbers[i])
        for j in range(1, max_num + 1):
            if ((int(numbers[i]) % j == 0) and (int(numbers[i - 1]) % j == 0)):
                gcd = j
print(gcd)    