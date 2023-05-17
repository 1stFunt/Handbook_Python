# Про остроту треугольника (остроугольный, тупоугольный, прямоугольный)
a = int(input())
b = int(input())
c = int(input())
M = [a, b, c]
max_num = max(M)
min_num = min(M)


def secondmax(numbers):
    numbers.remove(max(numbers))
    max_number = max(numbers)
    return max_number


sec_num = secondmax(M)
if max_num**2 == sec_num**2 + min_num**2:
    print("100%")
if max_num**2 > sec_num**2 + min_num**2:
    print("велика")
if max_num**2 < sec_num**2 + min_num**2:
    print("крайне мала")