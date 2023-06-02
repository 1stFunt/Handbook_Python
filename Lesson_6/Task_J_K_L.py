# J - На латинице.
dictionary = {'Ь': '', 'ь': '', 'Ъ': '', 'ъ': '', 'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v',
              'Г': 'G', 'г': 'g', 'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e', 'Ё': 'E', 'ё': 'e', 'Ж': 'Zh', 'ж': 'zh',
              'З': 'Z', 'з': 'z', 'И': 'I', 'и': 'i', 'Й': 'I', 'й': 'i', 'К': 'K', 'к': 'k', 'Л': 'L', 'л': 'l',
              'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r',
              'С': 'S', 'с': 's', 'Т': 'T', 'т': 't', 'У': 'U', 'у': 'u', 'Ф': 'F', 'ф': 'f', 'Х': 'Kh', 'х': 'kh',
              'Ц': 'Tc', 'ц': 'tc', 'Ч': 'Ch', 'ч': 'ch', 'Ш': 'Sh', 'ш': 'sh', 'Щ': 'Shch', 'щ': 'shch', 'Ы': 'Y',
              'ы': 'y', 'Э': 'E', 'э': 'e', 'Ю': 'Iu', 'ю': 'iu', 'Я': 'Ia', 'я': 'ia'}
text = list(input())


def match(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщыьэъюя')):
    return not alphabet.isdisjoint(text.lower()) # Проверка отсутствия общих элементов множества и последовательности
# возвращает True если отсутствует, но при операторе not - наоборот возвращает False

for word in text: 
    for v in word: 
        if match(v) is True:
            print(dictionary.get(v), end="")
        elif match(v) is False:
            print(v, end="")

# K - В первой строке указывается количество мужчин — сотрудников организации (N). 
# Затем идут N строк с фамилиями этих сотрудников в произвольном порядке.
# Количество однофамильцев в организации.
n = int(input())
secondname = [input() for i in range(n)]
result = 0
for i in set(secondname):  
    count = 0  
    for name in secondname:  
        if i == name:  
            count += 1  
    if count > 1:  
        result += count  
print(result)

# L - Однофамильцы 2.0 Список однофамильцев в организации с указанием их количества в алфавитном порядке.
n = int(input())
secondname = [input() for i in range(n)]
dct = {}
for sec_set in set(secondname):
    count = 0
    for sec_list in secondname:
        if sec_set == sec_list:
            count += 1
        if count > 1: 
            dct[sec_set] = count
if len(dct) > 0:
    for key, v in sorted(dct.items()):
        print(f"{key} - {v}")
else:
    print("Однофамильцев нет")