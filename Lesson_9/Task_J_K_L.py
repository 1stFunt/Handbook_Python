# J - Хвост. Формат ввода - Пользователь вводит имя файла (F),
# а затем количество строк (N), которые он хочет увидеть.
# Формат вывода - Выведите N последних строк файла F.
some_file = input()
num = int(input())

with open(some_file, "r", encoding="utf-8") as data:
    text = data.readlines()

for line in text[-num:]:
    print(line.replace("\n", ""))

"""
K - Напишите программу, которая для заданного файла вычисляет следующие параметры:
количество всех чисел;
количество положительных чисел;
минимальное число;
максимальное число;
сумма всех чисел;
среднее арифметическое всех чисел с точностью до двух знаков после запятой.
Формат ввода - Пользователь вводит два имени файла.
Первый файл содержит произвольное количество чисел, разделённых пробелами и символами перевода строки.
Формат вывода - Выведите статистику во второй файл в формате JSON.
Ключи значений задайте соответственно:
count — количество всех чисел;
_positivecount — количество положительных чисел;
min — минимальное число;
max — максимальное число;
sum — сумма всех чисел;
average — среднее арифметическое всех чисел с точностью до двух знаков после запятой.
"""
import json

file = input()
json_format = input()

with open(file, "r") as data:
    numbers = data.readlines()

result = []
for line in numbers:
    line_split = line.replace("\n", "").split()
    for num in line_split:
        result.append(int(num))

count = len(result)
positive_count = 0
for i in result:
    if i > 0:
        positive_count += 1
minimum = min(result)
maximum = max(result)
summa = sum(result)
average = round(summa / count, 2)
statistics = {"count": count,
              "positive_count": positive_count,
              "min": minimum,
              "max": maximum,
              "sum": summa,
              "average": average}

with open(json_format, "w", encoding="utf-8") as j:
    json.dump(statistics, j, ensure_ascii=False, indent="\t")

"""
L - Напишите утилиту, которая разделяет числа, записанные в файле, на три группы:
числа с преобладающим количеством чётных цифр;
числа с преобладающим количеством нечётных цифр;
числа с одинаковым количеством чётных и нечётных цифр.
Формат ввода - Пользователь вводит четыре имени файла.
Первый файл содержит произвольное количество чисел, разделённых пробелами и символами перевода строки.
Формат вывода - В три другие файла выведите числа, которые подходят под требуемое условие.
Сохраните положение чисел в строках.    
"""
n1 = input()
n2 = input()
n3 = input()
n4 = input()

with open(n1, mode="r", encoding="utf-8") as f1, \
     open(n2, mode="w", encoding="utf-8") as f2, \
     open(n3, mode="w", encoding="utf-8") as f3, \
     open(n4, mode="w", encoding="utf-8") as f4:
    lines = f1.readlines()

    for line in lines:
        nums = line.strip().split()
        nums_even = []
        nums_odd = []
        nums_multi = []

        for num in nums:
            kol_even = 0
            kol_odd = 0

            for s in num:
                if int(s) % 2 == 0:
                    kol_even += 1
                else:
                    kol_odd += 1

            if kol_even > kol_odd:
                nums_even.append(num)
            elif kol_odd > kol_even:
                nums_odd.append(num)
            else:
                nums_multi.append(num)

        f2.write(" ".join(nums_even) + "\n")
        f3.write(" ".join(nums_odd) + "\n")
        f4.write(" ".join(nums_multi) + "\n")