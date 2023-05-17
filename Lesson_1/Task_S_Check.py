# Красивый чек
x = str(input())  # Название товара
a = int(input())  # Цена товара
b = int(input())  # Вес товара
c = int(input())  # Количество денег у пользователя
sum = a * b
sum2 = c - sum
xxx = "="
space = " "
print("================Чек================")
print(f"Товар:{space * (35 - 6 - len(str(x)))}{x}")
print(f"Цена:{space * (35 - 5 - 11 - (len(str(b)) + len(str(a))))}{b}кг * {a}руб/кг")
print(f"Итого:{space * (35 - 6 - 3 - len(str(sum)))}{sum}руб")
print(f"Внесено:{space * (35 - 8 - 3 - len(str(c)))}{c}руб")
print(f"Сдача:{space * (35 - 6 - 3 - len(str(sum2)))}{sum2}руб")
print(f"{xxx}" * 35)