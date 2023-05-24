# P - Красивый вывод таблицы умножения.
def print_table(size, column_width):
    count_slash = 0
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            print(f"{i * j:^{column_width}}",
                  end="|" if count_slash < size - 1 else "")
            count_slash += 1
        count_slash = 0
        print()
        if i != size:
            print("-" * (size * (column_width + 1) - 1))


# Получаем размер таблицы и ширину столбцов из входных данных
size, column_width = int(input()), int(input())
print_table(size, column_width)

# Q - Требуется вывести общее количество палиндромов среди введённых чисел.
number = int(input())
counter = 0
for i in range(number):
    temp = input()
    rev = reversed(temp)
    if list(temp) == list(rev):
        counter += 1
print(counter)

# R - Новогодняя ёлка 2.0
n = int(input())
m = (-1 + (1 + 8 * n) ** 0.5) / 2
m = int(-1 * m // 1 * -1)

c = 0
elka = [[0] * i for i in range(1, m + 1)]

for i in range(m):
    for j in range(0, i + 1):
        if c < n:
            c += 1
            elka[i][j] = c
        else:
            elka[-1].remove(0)

max_len = len(str(' '.join(map(str, elka[-1]))))
 
for row in elka:
    print('{:^{width}}'.format((' '.join(map(str, row))), width=max_len))