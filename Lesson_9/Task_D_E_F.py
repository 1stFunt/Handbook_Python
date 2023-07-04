# D - Создайте программу, которая реализует маленький компонент поисковой системы.
# Формат ввода. Вводятся заголовки страниц.
# В последней строке записан поисковый запрос.
# Формат вывода. Вывести все заголовки страниц, в которых присутствует поисковый запрос (регистр не имеет значения).
# Порядок заголовков должен сохраниться.
from sys import stdin

# Читаем данные из stdin
lines = [line.rstrip("\n") for line in stdin]

# Итерируемся по строкам
for line in lines:
    if lines[-1].casefold() in line.casefold() and line != lines[-1]:
        print(line)

# E - Давайте теперь найдём все слова-палиндромы среди введённых строк.
# Формат вывода. Список слов-палиндромов в алфавитном порядке без повторений.
from sys import stdin

# Читаем данные из stdin
lines = [line.rstrip("\n") for line in stdin]

set_answer = set()
for line in lines:
    line_split = line.split()
    for i in line_split:
        if list(i.casefold()) == list(i.casefold()[::-1]): # list не обязателен
            if i not in set_answer:
                set_answer.add(i)

for i in sorted(set_answer):
    print(i)

# F - Транслитерация
# Формат ввода. В одной папке с вашей программой лежит файл cyrillic.txt. 
# В нём, в числе прочих, содержится некоторое количество кириллических символов.
# Формат вывода. В файл transliteration.txt записать результат транслитерации исходного файла   
dictionary = {'Ь': '', 'ь': '', 'Ъ': '', 'ъ': '', 'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v',
              'Г': 'G', 'г': 'g', 'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e', 'Ё': 'E', 'ё': 'e', 'Ж': 'Zh', 'ж': 'zh',
              'З': 'Z', 'з': 'z', 'И': 'I', 'и': 'i', 'Й': 'I', 'й': 'i', 'К': 'K', 'к': 'k', 'Л': 'L', 'л': 'l',
              'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r',
              'С': 'S', 'с': 's', 'Т': 'T', 'т': 't', 'У': 'U', 'у': 'u', 'Ф': 'F', 'ф': 'f', 'Х': 'Kh', 'х': 'kh',
              'Ц': 'Tc', 'ц': 'tc', 'Ч': 'Ch', 'ч': 'ch', 'Ш': 'Sh', 'ш': 'sh', 'Щ': 'Shch', 'щ': 'shch', 'Ы': 'Y',
              'ы': 'y', 'Э': 'E', 'э': 'e', 'Ю': 'Iu', 'ю': 'iu', 'Я': 'Ia', 'я': 'ia'}


def match(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщыьэъюя')):
    return not alphabet.isdisjoint(text.lower())


with open("cyrillic.txt", "r", encoding="utf-8") as data:
    text = data.readlines()

with open("transliteration.txt", "a", encoding="utf-8") as translate:
    for word in text:
        for v in word:
            if v.isalpha() and match(v) is True:
                print(dictionary.get(v), end="", file=translate)
            elif not v.isalpha() or match(v) is False:
                print(v, end="", file=translate)