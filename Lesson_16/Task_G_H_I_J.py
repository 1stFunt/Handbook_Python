# G - Представьте, что вы пишете компьютерную игру «Шахматы». Вам надо смоделировать шахматную доску,
# которая представляет собой матрицу. Чёрная клетка представляется нулём, а белая — единицей.
# Если смотреть на доску сверху, то левая верхняя клетка — белая.
# Напишите функцию make_board, которая принимает размер шахматной доски, и возвращает матрицу, моделирующую заданную доску.
# Установите тип элементов матрицы int8.
import numpy as np

def make_board(n: int):
    return np.array([[not (i + j) % 2 for i in range(n)] for j in range(n)], dtype=np.int8)


# H - Когда-то вы помогали детсадовцам с различными змейками. Давайте реализуем её на основе массивов.
# Напишите функцию snake, которая принимает ширину (m) и высоту (n) змейки, а также именованный параметр direction.
# Параметр direction могут принимать значения:
# H — горизонтальная змейка, используется по умолчанию;
# V — вертикальная змейка.
# Функция должна вернуть матрицу, представляющую змейку, с ячейками типа int16.
def snake(m, n, direction='H'):
    result = np.zeros((n, m), dtype=np.int16)
    k = 1
    if direction == 'H':
        for i in range(n):
            if i % 2 == 0:
                result[i, :] = np.arange(k, k + m)
            else:
                result[i, :] = np.arange(k + m - 1, k - 1, -1)
            k += m
    else:
        for i in range(m):
            if i % 2 == 0:
                result[:, i] = np.arange(k, k + n)
            else:
                result[:, i] = np.arange(k + n - 1, k - 1, -1)
            k += n
    return result

# I - Напишите функцию rotate, принимающую двумерную матрицу и один из углов поворота: 90°, 180°, 270° и 360°.
# Функция должна вернуть новую матрицу соответствующую заданному повороту по часовой стрелке.
import numpy as np

def rotate(matrix, angle):
    if angle == 90:
        return np.rot90(matrix, 1, (1, 0))
    elif angle == 180:
        return np.rot90(matrix, 2, (1, 0))
    elif angle == 270:
        return np.rot90(matrix, 3, (1, 0))
    elif angle == 360:
        return matrix
    
# J - Напишите функцию stairs, принимающую вектор и возвращающую матрицу, в которой каждая строка является 
# копией вектора со смещением.
import numpy as np

def stairs(vector):
    length = len(vector)
    matrix = np.zeros((length, length), dtype=int)
    for i in range(length):
        matrix[i, :] = np.roll(vector, i)
    return matrix