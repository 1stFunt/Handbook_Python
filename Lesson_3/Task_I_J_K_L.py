# I - Факториал
def factorial(num):
    fact = 1
    for i in range(2, num + 1):
        fact *= i
    return fact


number = int(input())
print(factorial(number))

# J - считаем по шагам в какие координаты попадём
direction = input()
stop_word = "СТОП"
coordinate_x = 0
coordinate_y = 0
while direction != stop_word:
    if direction == "СЕВЕР":
        coordinate_y += int(input())
    if direction == "ВОСТОК":
        coordinate_x += int(input())
    if direction == "ЮГ":
        coordinate_y -= int(input())
    if direction == "ЗАПАД":
        coordinate_x -= int(input())
    direction = input()
print(coordinate_y)
print(coordinate_x)

# K - Требуется вывести одно натуральное число — сумму цифр исходного
num = int(input())
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
print(sum)

# L - Требуется вывести одно натуральное число — максимальную цифру исходного
num = int(input())
max = 0
while (num != 0):
    if num % 10 > max:
        max = num % 10
    num = num // 10
print(max)

