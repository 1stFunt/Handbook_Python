# Сегодня в N часов M минут хозяин магазина заказал доставку нового товара. 
# Оператор сказал, что продукты доставят через T минут.
# Сколько будет времени на электронных часах, когда привезут долгожданные продукты?
a = int(input())
b = int(input())
c = int(input())
temp1 = a * 60 + b + c 
while temp1 >= 1440:
    temp1 -= 1440
a = temp1 // 60
temp2 = a * 60
b = temp1 - temp2
print(f"{str(a).zfill(2)}:{str(b).zfill(2)}")

# Второй способ
a = int(input())
b = int(input())
c = int(input())
temp1 = c // 60
temp2 = temp1 * 60
c = c - temp2
b = b + c
a = a + temp1
while b >= 60:
    b -= 60
    a += 1
while a >= 24:
    a = a - 24
print(f"{str(a).zfill(2)}:{str(b).zfill(2)}")