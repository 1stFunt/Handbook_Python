# E
price_of_product = float(input())
amount = 0
while price_of_product != int(0):
    if price_of_product < 500:
        amount += price_of_product
    elif price_of_product >= 500:
        amount += (price_of_product - (price_of_product / 100 * 10))
    price_of_product = float(input())
print(amount)

# F - Поиск НОД, алгоритм Евклида
def gcd(a, b):
    if a > b:
        temp = a
    else:
        temp = b
    for i in range(1, temp + 1): # В диапазоне от 1 до самого большого числа из двойки чисел.
        if ((a % i == 0) and (b % i == 0)):
            gcd = i
    return gcd


a = int(input())
b = int(input())
print(gcd(a, b))

# G - НОК двух данных чисел
a = int(input())
b = int(input())
min_number = min(a, b)
while True:
    if min_number % a == 0 and min_number % b == 0:
        break
    min_number += 1
print(min_number)

# H
string = input()
count = int(input())
print(f"{string}\n" * count) 