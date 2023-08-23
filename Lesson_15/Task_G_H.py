# G - При регистрации в различных сервисах пользователи вводят большое количество информации. 
# Правильное заполнение полей — важная часть работы программы, поэтому формы снабжают системами валидации данных.
# Напишите функцию name_validation, которая принимает один позиционный аргумент — фамилию или имя.
# Если параметр не является строкой, то вызовите исключение TypeError.
# А также разработайте собственные ошибки:
# CyrillicError — вызывается, если значение не состоит только из кириллических букв;
# CapitalError — вызывается, если значение не начинается с заглавной буквы или найдена заглавная буква 
# не в начале значения.
# Обработка ошибок должна происходить в порядке, указанном в задании.
class CyrillicError(Exception):
    pass 

class CapitalError(Exception):
    pass 

def name_validation(name):
    try:
        if not isinstance(name, str):
            raise TypeError
        if not all(i.casefold() in set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя") for i in name):
            raise CyrillicError
        if name != name.title() or any(i.isupper() for i in name if i != name[0]):
            raise CapitalError
    except TypeError:
        return "Вызвано исключение TypeError"
    except CyrillicError:
        return "Вызвано исключение CyrillicError"
    except CapitalError:
        return "Вызвано исключение CapitalError"
    return name 

print(name_validation("user"))

# H - Продолжим реализацию системы валидации.
# Напишите функцию userusername_validation, которая принимает один позиционный аргумент — имя пользователя:
# Если параметр не является строкой, то вызовите исключение TypeError.
# А также разработайте собственные ошибки:
# BadCharacterError — вызывается, если значение состоит не только из латинских букв, цифр и символа 
# нижнего подчёркивания;
# StartsWithDigitError — вызывается, если значение начинается с цифры.
# Обработка ошибок должна происходить в порядке, указанном в задании.
class BadCharacterError(Exception):
    pass 

class StartsWithDigitError(Exception):
    pass 

def username_validation(name):
    try:
        if not isinstance(name, str):
            raise TypeError
        if not all(i.casefold() in set("abcdefghijklmnopqrstuvwxyz1234567890_") for i in name):
            raise BadCharacterError 
        if name[0].isdigit():
            raise StartsWithDigitError
    except TypeError:
        return "Вызвано исключение TypeError"
    except BadCharacterError: 
        return "Вызвано исключение BadCharacterError"
    except StartsWithDigitError:
        return "Вызвано исключение StartsWithDigitError"
    return name 

print(username_validation("45_user"))