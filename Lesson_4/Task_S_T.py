# S - Требуется вывести сформированный числовой квадрат требуемого размера.
number = int(input())
if number > 18:
    format_string = '{:>2}'
else:
    format_string = '{}'

for i in range(number):
    for j in range(number):
        value = number - max(i, j, number - 1 - i, number - 1 - j)
        print(format_string.format(value), end=" ")
    print()

# T - Одно натуральное число из диапазона [2;10] — основание системы счисления с максимальной выгодой.
# Если таких оснований несколько, выбирается наименьшее.
def find_base(n: int) -> int:
    max_sum = 0
    max_base = 0
    for base in range(2, 11):
        num = n
        digits = []
        while num > 0:
            digits.append(num % base)
            num //= base
        cur_sum = sum(digits)
        if cur_sum > max_sum:
            max_sum = cur_sum
            max_base = base
    return max_base


print(find_base(int(input())))    