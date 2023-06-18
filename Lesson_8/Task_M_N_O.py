# M - Напишите программу, которая выводит список возможных расстановок спортсменов на старте.
# В первой строке задано натуральное число N — количество спортсменов. В следующих N строках записаны имена спортсменов.
# Отсортированный по алфавиту список расстановок. Имена в каждой строке выводить через запятую и пробел.
from itertools import permutations

number_of_peoples = int(input())
templist = []
for i in range(number_of_peoples): # или templist = [input() for _ in range(number_of_peoples)]
    name = input()
    templist.append(name)
for value in sorted(permutations(templist, number_of_peoples)):
    print(", ".join(value))

# N - В отличии от задачи M тут в мутации мы выводим не количество спортсменов, а 3, так как всего 3 призовых места.   
from itertools import permutations

number_of_peoples = int(input())
templist = []
for i in range(number_of_peoples):
    name = input()
    templist.append(name)
for value in sorted(permutations(templist, 3)): # Тут указываем 3 (так как всего 3 призовых места)
    print(", ".join(value))

# O - Формат ввода. В первой строке задано натуральное число N — количество членов семьи. В следующих N строках записаны желаемые 
# продукты (через запятую и пробел).
# Формат вывода. Варианты списков покупок в алфавитном порядке.
from itertools import chain, permutations

number_of_wishes = int(input())
full_list = []
for i in range(number_of_wishes):
    wishes = input().split(", ")
    full_list.append(wishes)
for value in sorted(permutations(chain.from_iterable(full_list), 3)):
    print(" ".join(value))