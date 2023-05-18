# Q - уберёт все чётные цифры из числа
number = list(map(int, input())) # разбиваем число на цифры и записываем в список
odd = [] # создаем новый список, куда будем складывать нечетные цифры
for i in range(len(number)):
    if number[i] % 2 == 1: # если нечетное
        odd.append(number[i]) # то закидываем это число в список odd
for num in odd:
    print(num, end="") # выводим список без пробелов

# R - Требуется составить математическое выражение — произведение простых неубывающих чисел,
# которое в результате даёт исходное
def factors(number, d=2):
    while number > 1:
        n1, n2 = divmod(number, d)
        if n2:
            d += 1
        else:
            yield d
            number = n1


n = int(input())
print(' * '.join(map(str, factors(n))))