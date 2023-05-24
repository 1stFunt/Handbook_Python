# D - Найти сумму цифр всех введённых чисел.
number = int(input())
sum = 0
for i in range(number):
    temp = int(input())
    while temp != 0:
        sum += temp % 10
        temp //= 10
print(sum)

# E - Вывести количество местностей, в которых есть зайка.
number = int(input())
rabbit_is_true = []  # создаем пустой список куда будем сувать заек
for i in range(number):
    counter = 0  # устанавливаем счетчик, который каждый раз будет обнуляться
    while (temp := input()) != "ВСЁ":  # до тех пор, пока введенное не ВСЁ
        if "зайка" in temp:  # ищем заек
            counter += 1  # если нашли, то counter == 1
            if counter == 1:  # устанавливаем ограничение, если число заек будет больше, считаться дальше не будет
                rabbit_is_true.append("зайка")  # суем зайку в список
print(rabbit_is_true.count("зайка"))  # выводим количество заек в нашем списке

# F - Поиск НОД — Алгоритм Эвклида.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


count = int(input())
gcd_value = 0
for i in range(count):
    num = int(input())
    if i == 0:
        gcd_value = num
    else:
        gcd_value = gcd(gcd_value, num)
print(gcd_value)
