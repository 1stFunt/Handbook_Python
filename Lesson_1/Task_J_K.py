# J - Воспитатель просит сделать программу, которая по имени ребенка и 
# номеру его шкафчика формирует «красивую» карточку для личного дела.
name = str(input())
number = int(input())
group = number // 100
order = number % 10
bed = number // 10 % 10
print(f"Группа №{group}.")
print(f"{order}. {name}.")
print(f"Шкафчик: {number}.")
print(f"Кроватка: {bed}.")

# K - Напишите программу для робота-няни, которая из числа вида abcd составляет число badc.
num = input() 
n_list = list(num) 
n1 = n_list[0]  # первая цифра
n2 = n_list[1]  # вторая цифра
n3 = n_list[2]  # третья цифра
n4 = n_list[3]  # четвертая цифра
newlist = [n2, n1, n4, n3]
number = "".join(newlist)
print(number)