# G - Лаборанты проводят эксперимент и запросили разработку системы обработки данных.
# Результатами эксперимента должны стать пары рациональных чисел.
# Для работы им требуются функции:
# enter_results(first, second, ...) — добавление данных одного или нескольких результатов
# (гарантируется, что количество параметров будет чётным);
# get_sum() — возвращает пару сумм результатов экспериментов;
# get_average() — возвращает пару средних арифметических значений результатов экспериментов.
# Все вычисления производятся с точностью до сотых.
def enter_results(*args):
    data.extend(args)


def get_sum():
    return (round(sum(data[::2]), 2), round(sum(data[1::2]), 2))


def get_average():
    return (round(sum(data[::2])/len(data[::2]), 2), round(sum(data[1::2])/len(data[1::2]), 2))


data = []

# H - Напишите lambda выражение для сортировки списка слов сначала по длине, а затем по алфавиту без учёта регистра.
string = 'Яндекс использует Python во многих проектах'
print(sorted(string.split(), key=lambda s: (len(s), s.casefold())))

# I - Напишите lambda выражение для фильтрации чисел с чётной суммой цифр.
print(*filter(lambda x: not sum(map(int, str(x))) % 2, (32, 64, 128, 256, 512)))

# P - Напишите функцию merge, которая принимает два отсортированных по возрастанию кортежа целых чисел, 
# а возвращает один из всех переданных чисел.
def secret_replace(text, **rules):
    keys_replaced = {}
    for key in rules.keys():
        keys_replaced[key] = 0
    i = 0
    temp_len = len(text)
    while i != temp_len:
        if text[i] in rules:
            old_char = text[i]
            if old_char not in keys_replaced:
                keys_replaced[old_char] = 0
            text = text[:i] + rules[old_char][keys_replaced[old_char]] + text[i + 1:]
            keys_replaced[old_char] += 1
            if keys_replaced[old_char] == len(rules[old_char]):
                keys_replaced[old_char] = 0
        i += 1
        temp_len = len(text)
    return text