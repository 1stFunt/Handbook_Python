# A - Напишите функцию make_list, которая создаёт, заполняет и возвращает список заданного размера.
def make_list(length, value=0, result=[]):
    for i in range(length):
        result.append(value)
    return result

# B - Напишите функцию make_matrix, которая создаёт, заполняет и возвращает матрицу заданного размера.
# size — кортеж (ширина, высота) или одно число (для создания квадратной матрицы);
# value — значение элементов списка (по-умолчанию 0).
def make_matrix(size, value=0):
    if isinstance(size, int):
        size = (size, size)
    return [[value] * size[0] for i in range(size[1])]
# или 
def make_matrix(size, value=0):
    result_matrix = []
    if isinstance(size, int):
        size = (size, size)
    for i in range(size[1]):
        result_matrix.append([value] * size[0])
    return result_matrix

# C - Функциональный нод 2.0
# Напишите функцию gcd, которая вычисляет наибольший общий делитель последовательности чисел.
# Параметрами функции выступают натуральные числа в произвольном количестве, но не менее одного.
def gcd(*numbers):
    import math
    return math.gcd(*numbers)
# или
def gcd_2(*numbers):
    def _gcd(a, b):
        if b == 0:
            return a
        return _gcd(b, a % b)

    result = numbers[0]
    for i in range(1, len(numbers)):
        result = _gcd(result, numbers[i])
    return result