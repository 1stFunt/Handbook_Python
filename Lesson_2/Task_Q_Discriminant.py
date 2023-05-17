# Вводится 3 вещественных числа a, b, c — коэффициенты уравнения вида: ax2(в квадрате) + bx + c = 0.
# Если у уравнения нет решений — следует вывести «No solution».
# Если корней конечное число — их нужно вывести через пробел в порядке возрастания с точностью до сотых.
# Если корней неограниченное число — следует вывести «Infinite solutions».
a = float(input())
b = float(input())
c = float(input())
x1 = float(0.00)
x2 = float(0.00)
if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
elif a == 0 and b != 0 and c != 0:
    x1 = -(c / b)   
    print(x1)
elif a == 0 and b == 0 and c != 0:
    print("No solution")
elif a == 0 and b != 0 and c == 0:
    x1 = 0
    print(x1)
else:
    disc = (b ** 2) - (4 * a * c)
    if disc == 0:
        x1 = (-b) / (2 * a)
        print(x1)
    elif disc > 0:
        x1 = (-b - (disc ** 0.5)) / (2 * a)
        x2 = (-b + (disc ** 0.5)) / (2 * a)
        print(min(x1, x2), max(x1, x2), sep=' ')
    elif disc < 0:
        print("No solution")