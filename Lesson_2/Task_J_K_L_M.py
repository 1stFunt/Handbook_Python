# # J - Пароль из трёхзначного числа по схеме: 
#       находится сумма цифр, стоящих в двух младших разрядах (десятки и единицы)
#       находится сумма цифр, стоящих в двух старших разрядах (сотни и десятки)
#       Эти две суммы, записанные друг за другом, в порядке не возрастания, формируют новое число
number = int(input())
sum1 = number // 10 % 10 + number % 10 # находим сумму цифр десяток и единиц в трехзначном числе
sum2 = number // 10 // 10 % 10 + number // 10 % 10 # аналогично для сотен и десяток
if (sum1 < sum2):
    print(f"{sum2}{sum1}")
else:
    print(f"{sum1}{sum2}")

# K - Красота числа по схеме:
# Если сумма его минимальной и максимальной цифр равна оставшейся цифре умноженной на 2
list_temp = list(map(int, input())) # разделить введенное число на элементы, присвоить им значение int и поместить в список
max_num = max(list_temp) # определить максимум
min_num = min(list_temp) # определить минимум
x_num = 0
for i in range(len(list_temp)): # двигаемся по списку
    if list_temp[i] < max_num and list_temp[i] > min_num: # если число меньше макс и больше мин
        x_num = list_temp[i] # то присваиваем ему значение x_num
if max_num + min_num == x_num * 2:
    print("YES")
else:
    print("NO")

# L - Про создание треугольника. В треугольнике любая сторона меньше суммы двух других.
number = int(input())
number2 = int(input())
number3 = int(input())
if (number < number2 + number3 and number2 < number + number3 and number3 < number + number2):
    print("YES")
else:
    print("NO")    

# M - Какая цифра общая в числах в одинаковой позиции?
number = int(input())
number2 = int(input())
number3 = int(input())
# разделяем числа на цифры
a = number // 10 % 10
b = number % 10
c = number2 // 10 % 10
d = number2 % 10
e = number3 // 10 % 10
f = number3 % 10
if (a == c and a == e):
    print(a)
elif (b == d and b == f):
    print(b)