# A - Напишите программу, которая проверяет, что первая буква во всех словах — А, Б или В.
number = int(input())
counter = 0
for i in range(number):
    temp = input()
    list_temp = list(temp)
    if list_temp[0] == "а" or list_temp[0] == "б" or list_temp[0] == "в":
        counter += 1
if counter == number:
    print("YES")
else:
    print("NO")

# B - Преобразует введённую стоку из горизонтальной записи в вертикальную.
text = input()
for i in text:
    print(i)

# C - Сокращённые заголовки.
length = int(input())
N = int(input())
list_temp = []
for i in range(N):
    temp = str(input())
    list_temp.append(temp)
for j in range(len(list_temp)):
    if len(list_temp[j]) > length: # если строка больше заданной длины
        print(f"{list_temp[j][:length - 3]}...") # срезаем строку до длины, убавляем еще 3, так как нужно вставить "..."
    elif len(list_temp[j]) <= length: # если же нет, то оставляем, как есть
        print(list_temp[j])