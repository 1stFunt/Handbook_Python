# S - Формат ввода
# В первой строке задается количество детей в группе (NN).
# В каждой из следующих NN строк записано имя ребенка и его игрушки в формате:
# Имя: игрушка1, игрушка2, ....
# Формат вывода
# Список игрушек, которые есть только у одного из детей в алфавитном порядке.
N = int(input())
toys = {}

for _ in range(N):
    name, *items = input().replace(",", "").split(" ")
    if name not in toys:
        toys[name] = set(items)
    else:
        toys[name].update(items)

result = set()
for val in toys.values():
    for toy in val:
        if sum(toy in v for v in toys.values()) == 1:
            result.add(toy)

for toy in sorted(result):
    print(toy)

# T - Напомним, что взаимно простыми называются числа, которые не имеют общих делителей кроме 1. 
# Напишите программу, которая для каждого переданного числа находит список его взаимно простых.
# Формат ввода
# Задана последовательность чисел записанных через точку с запятой (;) и пробел.
# Формат вывода
# Список чисел с указанием взаимно простых ему среди переданных.
# Все числа должны быть выведены в порядке возрастания без повторений.
# Строки следует отформатировать по правилу:
# число - взаимно простое 1, взаимно простое 2, ...
# Если для числа не было найдено ни одного взаимно простого, то и выводить его не требуется.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_coprime(a, b):
    return gcd(a, b) == 1


def coprime_numbers(numbers):
    coprime_dict = {}
    for i in range(len(numbers)):
        coprime_dict[numbers[i]] = set()
        for j in range(len(numbers)):
            if i != j and is_coprime(numbers[i], numbers[j]):
                coprime_dict[numbers[i]].add(numbers[j])
    for key in sorted(coprime_dict):
        if coprime_dict[key]:
            print(f"{key} - {', '.join(map(str, sorted(coprime_dict[key])))}")


numbers = input().split("; ")
numbers = list(map(int, numbers))
coprime_numbers(numbers)    