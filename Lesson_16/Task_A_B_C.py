# A - Напишите программу, которая вычисляет значение функции:
# f(x) = log32x^3/16 + x^cos(pi*x/2*e) - sin^2 x/pi
from math import log, pow, cos, e, pi, sin

def f(x):
    return log(pow(x, 3/16), 32) + pow(x, cos((pi * x) / (2 * e))) - sin(x / pi) ** 2

print(f(float(input())))

# B - Потоковый НОД
# Напишите программу, находящую наибольшие общие делители для всех переданных в стандартный поток 
# последовательностей чисел.
from math import gcd
from sys import stdin

lines = [list(map(int, line.rstrip("\n").split())) for line in stdin]

for i in [j for j in lines]:
    print(gcd(*i))

# С - Вася пришёл на образовательный семинар и обнаружил, что зрителей на мероприятии — N, а количество мест — M.
# Помогите Васе определить вероятность того, что он попадёт на семинар.
# Формат ввода
# Два числа N и M.
# Формат вывода
# Два числа — количество вариантов, в которых Вася попадает на семинар и количество всех вариантов групп на семинаре.
# Примечание
# В первом примере обозначим участников числами 1, 2, 3. Предположим, что 1 — это Вася.
import math

N, M = list(map(int, input().split()))

possible_ways_vasya = math.comb(N-1, M-1)
total_ways = math.comb(N, M)

probability = possible_ways_vasya / total_ways

print(possible_ways_vasya, total_ways)