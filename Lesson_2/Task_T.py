# Вывод. Строка в которой есть зайка, а затем её длина.
# Если таких строк несколько, выбрать ту, что меньше всех лексикографически.
str1 = input()
str2 = input()
str3 = input()
new_list = [str1, str2, str3]
rabbit_is_true = []
for i in range(len(new_list)):
    if "зайка" in new_list[i]:
        rabbit_is_true.append(new_list[i])
print(min(rabbit_is_true), len(min(rabbit_is_true)))