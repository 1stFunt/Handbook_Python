# D - Разработайте функцию month, которая принимает номер месяца и обозначение языка ("ru", "en") и 
# возвращает название заданного месяца в заданном языке с заглавной буквы.
def month(num, language):
    months_ru = {"1": "Январь", "2": "Февраль", "3": "Март", "4": "Апрель", "5": "Май", 
                 "6": "Июнь", "7": "Июль", "8": "Август", "9": "Сентябрь", "10": "Октябрь", 
                 "11": "Ноябрь", "12": "Декабрь"}
    months_eng = {"1": "January", "2": "February", "3": "March", "4": "April", "5": "May", 
                  "6": "June", "7": "July", "8": "August", "9": "September", "10": "October", 
                  "11": "November", "12": "December"}
    if language == "ru":
        return months_ru[str(num)]
    elif language == "en":
        return months_eng[str(num)]

# Тестер
for i in range(1, 13):
    print(month(i, "ru"))
    print(month(i, "en"))

# E - Разработайте функцию split_numbers, которая принимает строку целых чисел, разделённых пробелами, 
# и возвращает кортеж из этих чисел.
def split_numbers(string):
    string = tuple(map(int, string.split()))
    return string

# F - Разработайте функцию modern_print, которая принимает строку и выводит её, если она не была выведена ранее.
def modern_print(string):
    if string not in new_set:
        print(string)
        new_set.add(string)

        
new_set = set()

# G - Напишите функцию can_eat, которая принимает положение коня и другой фигуры в виде кортежей из двух координат, 
# а возвращает булево значение: True если конь съедает фигуру и False иначе.
def can_eat(knight_pos, figure_pos):
    x1, y1 = knight_pos
    x2, y2 = figure_pos

    # Конь может съесть фигуру только если она расположена в одном из 8 возможных полей
    return abs(x1 - x2) == 2 and abs(y1 - y2) == 1 or abs(x1 - x2) == 1 and abs(y1 - y2) == 2