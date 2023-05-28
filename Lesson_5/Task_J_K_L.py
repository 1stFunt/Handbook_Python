# J - Выводится один символ в нижнем регистре — наиболее часто встречающийся.
answer = "" 
counter = 0 
dct = {}
while True:
    temp = input()
    n = temp.upper()
    for now in n:
        if now not in dct:
            dct[now] = 0 # символ становится ключом со значением 0
        dct[now] += 1
    for key in dct: # перебор символов, которые стали ключами
        if key != " ":
            if dct[key] > counter: # сравнение значения ключа с счётчиком
                counter = dct[key]
                answer = key
            elif dct[key] == counter:
                if key < answer: # сравнение в алфавитном порядке
                    answer = key 
    if temp == "ФИНИШ":
        break
print(answer.lower())

# K - Вывести все заголовки страниц, в которых присутствует поисковый запрос (регистр не имеет значения).
# Порядок заголовков должен сохраниться.
number = int(input())
list_temp = []
for i in range(1, number + 1):
    temp = input()
    list_temp.append(temp)
    if i >= number:
        yandex = input()
        for string in list_temp:
            if yandex.lower() in string.lower():
                print(string)

# L - Вводится натуральное число N — количество дней. Вывести список каш в порядке подачи.
number = int(input())
list_temp = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
new_list = []
index = 0
for i in range(number):
    new_list.append(list_temp[index])
    index += 1
    print(new_list[i])
    if index == len(list_temp):
        index = 0