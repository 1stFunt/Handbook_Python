# H - Напишите функцию update, которая добавляет к данным столбец average, содержащий среднюю оценку ученика,
# а также сортирует данные по убыванию этого столбца, а при равенстве средних — по имени лексикографически.
import pandas as pd

def update(journal):
    # Добавляем столбец average
    journal['average'] = journal[['maths', 'physics', 'computer science']].mean(axis=1)
    # Сортируем данные по столбцу average в убывающем порядке
    # и при равенстве средних по имени лексикографически
    filtered = journal.sort_values(by=['average', 'name'], ascending=[False, True])
    # Удаляем столбец average из исходного DataFrame
    journal.drop(columns=['average'], inplace=True)
    return filtered

columns = ['name', 'maths', 'physics', 'computer science']
data = {
    'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
    'maths': [5, 4, 5, 2, 4],
    'physics': [4, 4, 4, 5, 5],
    'computer science': [5, 2, 5, 4, 3]
}
journal = pd.DataFrame(data, columns=columns)
# Вызываем функцию update
filtered = update(journal)
# Выводим исходный и отфильтрованный DataFrame
print(journal)
print(filtered)

# I - Бесконечный морской бой
# Представьте себе поле морского боя, которое не имеет границ. 
# Для простоты координаты выстрелов будем обозначать целыми координатами на плоскости.
# Бесконечное поле порождает большое количество данных, которые требуется проанализировать. 
# Один из игроков для упрощения этой задачи просит вас написать программу, которая обрезает данные до ограниченного прямоугольника.
# Формат ввода
# В первой строке записано два числа — координаты верхнего левого угла. Во второй строке — правого нижнего.
# В файле data.csv находится датасет с координатами всех выстрелов противника.
# Формат вывода
# Часть датасета, ограниченная заданным прямоугольником.
import pandas as pd

# Чтение данных из файла data.csv
df = pd.read_csv('data.csv')
# Чтение координат верхнего левого угла и правого нижнего угла
top_left_x, top_left_y = map(int, input().split())
bottom_right_x, bottom_right_y = map(int, input().split())
# Фильтрация данных внутри заданного прямоугольника
filtered_data = df[(df['x'] >= top_left_x) & (df['x'] <= bottom_right_x) & (
    df['y'] >= bottom_right_y) & (df['y'] <= top_left_y)]
# Вывод отфильтрованных данных
print(filtered_data)

# J - Экстремум в математике — максимальное или минимальное значение функции на заданном множестве.
# Чаще всего математики для поиска экстремума функции прибегают к её дифференцированию. 
# Однако мы можем обойти этот трудоёмкий процесс и схитрить.
# Напишите три функции:
# values(func, start, end, step), строящую Series значений функции в точках диапазона и принимающую:
# функцию одной переменной;
# начало диапазона;
# конец диапазона;
# шаг вычисления;
# min_extremum(data) возвращает точку, в которой был достигнут минимум на диапазоне;
# max_extremum(data) возвращает точку, в который был достигнут максимум на диапазоне
import pandas as pd
import numpy as np

# Функция для создания Series значений функции в заданном диапазоне с заданным шагом
def values(func, start, end, step):
    x = np.arange(start, end + step, step)
    y = func(x)
    return pd.Series(y, index=x)
# Функция для нахождения точки, в которой достигается минимум
def min_extremum(data):
    min_value = data.min()
    min_index = data[data == min_value].index
    if len(min_index) == 0:
        return None
    return min_index[0]
# Функция для нахождения точки, в которой достигается максимум
def max_extremum(data):
    max_value = data.max()
    max_index = data[data == max_value].index
    if len(max_index) == 0:
        return None
    return max_index[0]
# Пример использования
data = values(lambda x: x ** 2 + 2 * x + 1, -1.5, 1.7, 0.1)
print(data)
print(min_extremum(data))
print(max_extremum(data))