# J - Аня, Боря и Вова решили съесть апельсин.
# Подскажите ребятам, как им его разделить.
# Разработайте программу, которая выводит все возможные способы разделки апельсина.
# Формат ввода - В единственной строке записано количество долек апельсина (N).
# Формат вывода - Таблица вариантов разделения апельсина.
from itertools import product

number = int(input())
print("А Б В")
# Генерация всех возможных комбинаций троек чисел от 1 до number
combinations = product(range(1, number+1), repeat=3)
# Перебор и вывод комбинаций
for i, j, k in combinations:
    if i + j + k == number:
        print(i, j, k)
# или 
number = int(input())
print("А Б В")
for i in range(1, number):
    for j in range(1, number):
        for k in range(1, number):
            if number - (i + j + k) == 0:
                print(i, j, k)

# K - Формат ввода - В первой строке записано число N — высота числового прямоугольника.
# Во второй строке указано число M — ширина числового прямоугольника.
# Формат вывода - Нужно вывести сформированный числовой прямоугольник требуемого размера.
# Чтобы прямоугольник был красивым, каждый его столбец должен быть одинаковой ширины.  
from itertools import product

h = int(input())
w = int(input())
numbers = list(range(1, h * w + 1))
for i, j in product(range(h), range(w)):
    index = i * w + j
    print(f"{numbers[index]:>{len(str(h * w))}}", end=" " + ("\n" if j == (w - 1) else ""))

# L - Формат ввода. В первой строке задано натуральное число N — количество членов семьи. В следующих NN строках записаны 
# желаемые продукты (через запятую и пробел).
# Формат вывода. Отсортированный по алфавиту список продуктов с нумерацией.
# Примечание. Помните, что итераторы можно хранить в списке, а его можно распаковать в любую функцию.     
from itertools import chain

number_of_people = int(input())
temp = []
for i in range(number_of_people):
    wishes = list(input().split(", "))
    temp.append(wishes)
for index, value in enumerate(sorted(temp), 1):
    print(f'{index}. {value}')        