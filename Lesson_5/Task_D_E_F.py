# D - Напишите программу, которая избавляется от:
# Двух символов # в начале информационных сообщений;
# Строк, заканчивающихся тремя символами @
list_temp = []
while True: # бесконечный цикл в котором все, что мы будем вписывать в терминал, попадет в список list_temp
    temp = input()
    list_temp.append(temp)
    if temp == "": # если введена пустая строка, остановить цикл
        break
del list_temp[-1] # удаляем последний элемент, так как это пустая строка
new_list = []
for string in list_temp:
    if string[0] == "#" and string[1] == "#" and string[-1] != "@": # если первые 2 элемента это #, то удалим их lstrip
        new_list.append(string.lstrip("#"))
    elif string[-1] != "@" and string[-2] != "@" and string[-3] != "@": # если последние элементы не @, оставляем как есть
        new_list.append(string)
for i in range(len(new_list)): 
    print(new_list[i]) # выводим полученные очищенные строки

# E - Палиндром.
string = input()
rev = reversed(string) # возвращается обратный интератор, поэтому нужно поместить rev в list() для правильной работы
if list(string) == list(rev):
    print("YES")
else:
    print("NO")

# F - Ищем кол-во заек.
number = int(input())
counter = 0
for i in range(number):
    temp = input()
    counter += temp.count("зайка")
print(counter)