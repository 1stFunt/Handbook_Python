"""      
G - Напишите программу, которая для заданного файла вычисляет следующие параметры:
количество всех чисел;
количество положительных чисел;
минимальное число;
максимальное число;
сумма всех чисел;
среднее арифметическое всех чисел с точностью до двух знаков после запятой.
Формат ввода - Пользователь вводит имя файла.
Файл содержит произвольное количество чисел, разделённых пробелами и символами перевода строки.
Формат вывода - Выведите статистику в указанном порядке.
"""
file = input()

with open(file, "r") as data:
    numbers = data.readlines()

result = []
for line in numbers:
    line_split = line.rstrip("\n").split()
    for num in line_split:
        result.append(int(num))

the_number_of_positive = 0

# Количество чисел:
print(len(result))

# Количество положительных чисел:
for num in result:
    if num > 0:
        the_number_of_positive += 1
print(the_number_of_positive)

# Минимальное число:
print(min(result))

# Максимальное число:
print(max(result))

# Сумма всех чисел:
print(sum(result))

# Среднее арифметическое:
print(round(sum(result) / len(result), 2))

# H - Напишите программу, которая определяет, какие слова есть только в одном из файлов.
# Формат ввода - Пользователь вводит три имени файлов.
# Каждый из входных файлов содержит произвольное количество слов, 
# разделённых пробелами и символами перевода строки.
# Формат вывода - В третий файл выведите в алфавитном порядке без повторений список слов, 
# которые есть только в одном из файлов.
first = input()
second = input()
answer = input()

with open(first, "r", encoding="utf-8") as f:
    first_text = f.readlines()

with open(second, "r", encoding="utf-8") as s:
    second_text = s.readlines()

result_for_first = set()
for line in first_text:
    line_split = line.replace("\n", "").split()
    for word in line_split:
        result_for_first.add(word)

result_for_second = set()
for line in second_text:
    line_split = line.replace("\n", "").split()
    for word in line_split:
        result_for_second.add(word)

with open(answer, "a", encoding="utf-8") as a:
    set_answer = result_for_first ^ result_for_second
    for word in sorted(set_answer):
        print(word, file=a)

"""
I - Напишите простую утилиту, которая очищает заданный файл от:
повторяющихся пробелов;
повторяющихся символов перевода строки;
табуляций,
излишних пробелов в начале и конце строк.
Формат ввода - Пользователь вводит два имени файлов.
Входной файл содержит неформатированный текст произвольной длины.
Формат вывода - Во второй файл выведите очищенный текст.
"""
def clean_text(input_file, output_file):
    # читаем файл построчно
    with open(input_file, 'r', encoding='utf-8') as f_in:
        lines = f_in.readlines()

    # очищаем каждую строку
    cleaned_lines = []
    for line in lines:
        # удаляем лишние пробелы в начале и конце строки
        line = line.strip()
        # удаляем повторяющиеся пробелы и все табуляции
        line = ' '.join(line.replace("\t", "").split())
        if line:
            # добавляем перевод строки, если строка не пустая
            cleaned_lines.append(line + '\n')
        else:
            # иначе добавляем пустую строку
            cleaned_lines.append(line)

    # записываем очищенный текст в файл
    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.writelines(cleaned_lines)

# спрашиваем у пользователя имена файлов
input_file = input()
output_file = input()

# вызываем функцию для очистки текста
clean_text(input_file, output_file)