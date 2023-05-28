# G - Два целых числа, разделённые пробелом. Одно целое число — сумма переданных чисел.
print(sum((map(int, input().split(" "))))) # создаем список с элементами через пробел, 
                                           # присваиваем каждому элементу тип int, и суммируем

# H - Поиск заек в строках (положение первого зайки)  
number = int(input())
list_temp = []
for i in range(number):
    temp = input()
    list_temp.append(temp)
for string in list_temp:
    if "зайка" in string:
        print(string.index("зайка") + 1) # указываем индекс первого вхождения зайки
    else:
        print("Заек нет =(")     

# I - Каждую строку нужно очистить от комментариев.
# А если комментарий — вся строка, то выводить её не надо.             
list = []

while True:
    line = input()
    if line == '':
        break
    else:
        list.append(line)

for line in list:
    grid = line.find('#')
    if grid == 0:
        continue
    if grid > 0:
        print(line[:grid])
    else:
        print(line)