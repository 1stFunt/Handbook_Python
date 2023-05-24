# G - Обратный отсчёт.
number = int(input())
temp = 3
for i in range(number):
    j = 0
    while j < temp:
        print(f"До старта {temp - j} секунд(ы)")
        j += 1
    temp += 1
    print(f"Старт {i + 1}!!!")

# H - Вывести победителя с наибольшой суммой цифр числа.
number = int(input())
maximum = 0
for i in range(number):
    tempname = input()  # вводим имя ребенка
    tempnumber = int(input())  # его число
    summa = 0
    while tempnumber != 0:  # считаем сумму цифр в числе в цикле
        summa += tempnumber % 10
        tempnumber //= 10
        if summa > maximum:  # проверяем на максимум
            maximum = summa
            maxname = tempname
        if summa == maximum:
            maxname = tempname
print(maxname)

# I - Одно большое число.
number = int(input())
numbers = []
for i in range(number):
    temp = int(input())
    maximum = int(max(str(temp))) # переводим число в строчный формат, определяем его максимум и возвращаем int значение
    numbers.append(maximum) # закидываем эту цифру в список
for j in range(len(numbers)):
    print(f"{numbers[j]}", end="") # выводим из списка цифры