# N - составить из трёхзначного числа минимально и максимально возможные двухзначные числа
number = int(input())
a = number // 10 // 10 % 10
b = number // 10 % 10
c = number % 10
M = [a, b, c]
max_num = max(M)
min_num = min(M)


def secondmax(numbers):
    numbers.remove(max(numbers))  # удаляем максимум прошлый
    max_number = max(numbers)  # создаем новый максимум
    return max_number  # возвращаем это значение


second_max = secondmax(M)
if (min_num == 0):
    print(f"{second_max}{min_num} {max_num}{second_max}")
else:
    print(f"{min_num}{second_max} {max_num}{second_max}")

# O - первой взять максимальную цифру из всех защитных чисел
# последней — минимальную
# в середину поставить сумму оставшихся без учёта переноса разряда
number = int(input())
number2 = int(input())
a = number // 10 % 10
b = number % 10
c = number2 // 10 % 10
d = number2 % 10
M = [a, b, c, d]
max_num = max(M)
min_num = min(M)

def secondmax(numbers):
    numbers.remove(max(numbers))
    max_number = max(numbers)
    return max_number

def secondmin(numbers):
    numbers.remove(min(numbers))
    min_number = min(numbers)
    return min_number

sec_max = secondmax(M)
sec_min = secondmin(M)
sum = sec_max + sec_min
print(f"{max_num}{sum % 10}{min_num}")

# P - Красивый вывод
space = " "
name = ["Петя", "Вася", "Толя"]
tempname = ["", "", ""]
speed = [0, 0, 0]
speed[0] = int(input())
speed[1] = int(input())
speed[2] = int(input())
for i in range(len(speed)):
    tempname[i] = name[speed.index(max(speed))]
    speed[speed.index(max(speed))] = 0

print(f'{space * 10}{tempname[0]}')
print(f'{space * 2}{tempname[1]}')
print(f'{space * 18}{tempname[2]}')
print(f'{space * 3}II{space * 6}I{space * 6}III')