# G - Азбука Морзе
dictionary = {'A': '.-', 'B': '-...', 'C': '-.-.',
              'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..',
              'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-',
              'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..',
              '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....',
              '6': '-....', '7': '--...', '8': '---..',
              '9': '----.'}
text = input().upper().split(" ")
for word in text:
    for v in word:
        print(dictionary.get(v), end=" ")
    print()

# H - Кашееды — 4.0
# В первой строке задаётся количество детей в группе N. 
# В следующих N строках записана фамилия ребенка и список его любимых каш. 
# В последней строке записана каша, информацию о которой хочет получить воспитатель.
# Фамилии учеников, которые любят заданную кашу, в алфавитном порядке.
N = int(input())
kasha = dict()
for i in range(N):
    secondname = input().split(" ")
    name = secondname[0]
    kasha_keys = secondname[1:]
    for each in kasha_keys:
        if each not in kasha:
            kasha[each] = [name]
        else:
            kasha[each].append(name)
selected_kasha = input()
answer = []
if selected_kasha in kasha:
    for name in kasha[selected_kasha]:  # или - answer = kasha.get(selected_kasha, [])
        answer.append(name)             # или - for i in range(len(kasha[selected_kasha])):
                                        #           answer.append(kasha[selected_kasha][i])
else:
    print("Таких нет")
for j in sorted(answer):
    print(j)    

# I - В каждой строке записано описание придорожной местности. Конец ввода обозначается пустой строкой.
# Список увиденного и их количество. Порядок вывода не имеет значения.
dct = {}
while True:
    rabbit = input()
    temp = rabbit.split(" ")
    for r in temp:
        if r not in dct:
            dct[r] = 0
        dct[r] += 1
    if rabbit == "":
        break
for key, value in dct.items():
    if key != "":
        print(key, value)    