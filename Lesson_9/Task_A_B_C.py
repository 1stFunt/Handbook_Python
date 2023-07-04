# A - Напишите программу, которая находит сумму всех чисел введённых пользователем.
from sys import stdin

lines = []
for line in stdin:
    lines.append(line.rstrip(" \n"))

summa = 0
for string in lines:
    numbers = list(map(int, string.split()))
    for num in numbers:
        summa += num
print(summa)

# B - Напишите программу, которая определяет, на сколько изменился средний рост учеников в классе.
# Формат ввода. Вводится информация о детях в формате:
# <Имя> <Рост месяц назад> <Рост сейчас>
# Формат вывода. Одно число — ответ на вопрос задачи.
# Ответ округлите до целых. Например, функцией round.
from sys import stdin

lines = []
for line in stdin:
    lines.append(line.rstrip(" \n"))

summa = 0
for line in lines:
    first = int(line.split()[1])
    second = int(line.split()[2])
    diff = second - first
    summa += diff
print(round(summa / len(lines)))

# C - когда вы комментируете свой код, перед его выполнением интерпретатор удаляет комментарии.
# Напишите программу, которая выполняет данную функцию за интерпретатор.
# Формат ввода. Вводятся строки программы.
# Формат вывода. Каждую строку нужно очистить от комментариев.
# А если комментарий — вся строка, то выводить её не нужно.
from sys import stdin

# Читаем данные из stdin
lines = [line.rstrip("\n") for line in stdin]

# Итерируемся по строкам
for line in lines:
    # Находим первое вхождение символа #
    hash_index = line.find('#')
    # Если символ отсутствует, выводим строку
    if hash_index == -1:
        print(line)
    # Иначе выводим строку до символа #
    else:
        stripped_line = line[:hash_index].rstrip()
        if stripped_line != "":
            print(stripped_line)