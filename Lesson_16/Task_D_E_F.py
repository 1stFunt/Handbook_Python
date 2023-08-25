# D - G(x^1, x^2, x^3... x^n) = scrt(n(x^1 * x^2 * ... x^n)) = П(n, i=1(xi))**1/n
import statistics

numbers = list(map(float, input().split()))
print(statistics.geometric_mean(numbers))

# E - Два выдуманных человечка Дека и Поля, пользуются каждый своей системой координат. 
# Деке нравится представлять себя в декартовом пространстве, а Поле — в полярном.
# Напишите программу, определяющую кротчайшее расстояние, которое нужно пройти Деке и Поле, чтобы встретиться.
# Формат ввода
# В первой строке записаны координаты Деки: два рациональных числа — x и y
# Во второй строке записаны координаты Поли: два рациональных числа — p и ϕ
# Формат вывода
# Одно число — расстояние между Декой и Полей.
# Примечание
# Дека и Поля живут на одной плоскости с общим центром.
import numpy as np

def polar_to_dekart(polar_x, polar_y):
    x = polar_x * np.cos(polar_y)
    y = polar_x * np.sin(polar_y)
    return x, y

def shortest_distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

x1, y1 = map(float, input().split())
polar_x, polar_y = map(float, input().split())
x2, y2 = polar_to_dekart(polar_x, polar_y)

print(shortest_distance(x1, y1, x2, y2))

# F - Напишите функцию multiplication_matrix, которая принимает размер матрицы (N) и 
# возвращает массив описывающий таблицу умножения N на N.
import numpy as np

def multiplication_matrix(n):
    return np.array([[(i + 1) * (j + 1) for j in range(n)] for i in range(n)])