# A - Функциональное приветствие
# В решении не должно быть вызовов требуемых функций.
def print_hello(name):
    print(f"Hello, {name}!")

# B - Напишите функцию gcd, которая принимает два натуральных числа и возвращает их наибольший общий делитель.
def gcd(a, b):
    if a > b:
        temp = a
    else:
        temp = b
    for i in range(1, temp + 1):
        if ((a % i == 0) and (b % i == 0)):
            gcd = i
    return gcd

def gcd(a, b):
    import math
    return math.gcd(a, b)

# C - Разработайте функцию number_length, которая принимает одно целое число и возвращает его длину без учёта знака.
def number_length(num):
    num = num * -1 if num < 0 else num
    return len(str(num))  