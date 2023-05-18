# M - Ходит тот, чьё имя короче
number_of_players = int(input())
array = list()
for i in range(number_of_players):
    name = input()
    array.append(name)
print(min(array))

# N - Требуется вывести сообщение YES если число простое, иначе — NO
import math
number = int(input())
counter = 0
if number > 1:
    for i in range(2, int(math.sqrt(number) + 1)):
        if (number % i == 0):
            counter += 1
            break 
    if counter == 0:
        print("YES")
    else:
        print('NO')
else:
    print('NO')

# O - Количество строк, в которых есть зайка
number_of_str = int(input())
counter = 0
for i in range(number_of_str):
    if "зайка" in input():
        counter += 1
print(counter)

# P - YES — если число является палиндромом, иначе — NO
number = input()
rev = reversed(number)

if list(number) == list(rev):
    print("YES")
else:
    print("NO")