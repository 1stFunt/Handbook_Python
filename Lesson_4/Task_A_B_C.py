# A - Таблица умножения заданного размера.
number = int(input())
for i in range(1, number + 1):
    for j in range(1, number + 1):
        print(f"{i * j}", end=" ")
    print()

# B - Таблица умножения в виде списка.
number = int(input())
for i in range(1, number + 1):
    for j in range(1, number + 1):
        print(f'{j} * {i} = {i * j}')

# C - Ёлка
number = int(input())

current_number = 1
for i in range(1, number + 1):
    for j in range(i):
        if current_number > number:
            break
        print(current_number, end=" ")
        current_number += 1
    print()
    if current_number > number:
        break