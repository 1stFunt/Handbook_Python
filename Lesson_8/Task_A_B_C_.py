# A - Вводится одна строка.
# Требуется вывести нумерованный список, составленный из её слов.
string = input().split(" ")
for index, value in enumerate(string, 1):
    print(f'{index}. {value}')

# B - Вводится две строки с именами детей, записанными через запятую и пробел.
# Требуется вывести список пар, которые можно составить, если последовательно брать из каждой шеренги по одному ребёнку.
# Имена в парах выводить через дефис окружённый пробелами    
kids = list(zip(input().split(", "), input().split(", ")))
for i in kids:
    print(" - ".join(i))

# C - Напишите программу, которая производит счёт по заданным параметрам.
# В одну строку через пробел вводятся 3 рациональных числа — начало счета, конец и шаг.
# Последовательность чисел с заданными параметрами.
from itertools import count

start_end_step = list(map(float, input().split(" ")))
start = start_end_step[0]
end = start_end_step[1]
step = start_end_step[2]
for value in count(start, step):
    if value <= end:
        print(round(value, 2))
    else:
        break    