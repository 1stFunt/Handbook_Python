# G - Формат ввода
# В первой строке записано число учеников (N). В каждой из последующих N строк записано одно имя.
# Формат вывода
# Список игр в формате: <Игрок 1> - <Игрок 2> Порядок игр не имеет значения.
from itertools import combinations
number_of_players = int(input())
names = [input() for name in range(number_of_players)]
for n1, n2 in list(combinations(names, 2)):
    print(f'{n1} - {n2}')

# H - Напишите программу, которая строит расписание каш на ближайшие дни.
# Формат ввода
# Вводится натуральное число M — количество каш в меню. В каждой из последующих M строк записано одно название каши. 
# В конце передается натуральное число N — количество дней.
# Формат вывода
# Вывести список каш в порядке подачи.
from itertools import islice, repeat, chain

number_of_kashas = int(input())
kashas = [input() for kasha in range(number_of_kashas)]
number_of_days = int(input())
temp = number_of_days // number_of_kashas  # без переменной temp тоже работает верно
for i in list(islice(chain.from_iterable(repeat(kashas, temp + 1)), number_of_days)):
    print(i)

# I - Формат ввода. Вводится одно натуральное число — требуемый размер таблицы.
# Формат вывода. Таблица умножения заданного размера.
# Примечание. itertools.product отличный способ, чтобы избавиться от вложенных циклов.
from itertools import product

num = int(input())
for i, j in product(range(1, num + 1), repeat=2):
    print(i * j, end=" " + ("\n" if j == num else ""))    