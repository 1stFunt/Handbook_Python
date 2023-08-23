# Используйте две предыдущих функции валидации и напишите функцию user_validation, которая принимает 
# именованные аргументы:
# last_name — фамилия;
# first_name — имя;
# username — имя пользователя.
# Если функции был передан неизвестный параметр или не передан один из обязательных, то вызовите исключение KeyError.
# Если один из параметров не является строкой, то вызовите исключение TypeError.
# Обработка данных должна происходить в порядке: фамилия, имя, имя пользователя.
# Если поле заполнено верно, функция возвращает словарь с данными пользователя.
class CyrillicError(Exception):
    pass 

class CapitalError(Exception):
    pass 

class BadCharacterError(Exception):
    pass 

class StartsWithDigitError(Exception):
    pass 

def user_validation(**kwargs):
    try:
        if len(kwargs) != 3:
            raise KeyError
        if not all(isinstance(val, str) for val in kwargs.values()):
            raise TypeError
        last_name = kwargs.get('last_name')
        first_name = kwargs.get('first_name')
        username = kwargs.get('username')
        if not all(i.casefold() in set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя") for i in last_name):
            raise CyrillicError
        if last_name != last_name.title() or any(i.isupper() for i in last_name if i != last_name[0]):
            raise CapitalError
        if not all(i.casefold() in set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя") for i in first_name):
            raise CyrillicError
        if first_name != first_name.title() or any(i.isupper() for i in first_name if i != first_name[0]):
            raise CapitalError
        if not all(i.casefold() in set("abcdefghijklmnopqrstuvwxyz1234567890_") for i in username):
            raise BadCharacterError
        if username[0].isdigit():
            raise StartsWithDigitError
    except KeyError:
        return "Вызвано исключение KeyError"
    except TypeError:
        return "Вызвано исключение TypeError"
    except CyrillicError:
        return "Вызвано исключение CyrillicError"
    except CapitalError:
        return "Вызвано исключение CapitalError"
    except BadCharacterError:
        return "Вызвано исключение BadCharacterError"
    except StartsWithDigitError:
        return "Вызвано исключение StartsWithDigitError"
    return {"last_name": last_name, "first_name": first_name, "username": username}

print(user_validation(last_name="Иванов", first_name="Иван", username="ivanych45", password="123456"))
print(user_validation(last_name="Иванов", first_name="Иван", username="ivanych45"))

# I - После того как пользователь ввёл свои данные в требуемом формате, можно позаботиться и о пароле.
# Напишите функцию password_validation, которая принимает один позиционный параметр — пароль, и следующие 
# именованные параметры:
# min_length — минимальная длина пароля, по умолчанию 8;
# possible_chars — строка символов, которые могут быть в пароле, по умолчанию латинские буквы и цифры;
# at_least_one — функция возвращающая логическое значение, по умолчанию str.isdigit.
# Если переданный позиционный параметр не является строкой, вызовите исключение TypeError.
# А так же реализуйте собственные исключения:
# MinLengthError — вызывается, если пароль меньше заданной длины;
# PossibleCharError — вызывается, если в пароле используется недопустимый символ;
# NeedCharError — вызывается, если в пароле не найдено ни одного обязательного символа.
# Проверка условий должна происходить в порядке указанном в задании.
# Так как, хороший разработчик никогда не хранит пароли в открытом виде, функция, в случае успешного 
# завершения, возвращает хеш пароля. Для этого воспользуйтесь функцией sha256 из пакета hashlib и верните 
# его шестнадцатеричное представление.
import hashlib

class MinLengthError(Exception):
    pass

class PossibleCharError(Exception):
    pass

class NeedCharError(Exception):
    pass

def password_validation(password, min_length=8,
                        possible_chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
                        at_least_one=str.isdigit):
    try:
        if not isinstance(password, str):
            raise TypeError
        if len(password) < min_length:
            raise MinLengthError
        if not all(i in possible_chars for i in password):
            raise PossibleCharError
        if not any(at_least_one(i) for i in password):
            raise NeedCharError
    except TypeError:
        return "Вызвано исключение TypeError"
    except MinLengthError:
        return "Вызвано исключение MinLengthError"
    except PossibleCharError:
        return "Вызвано исключение PossibleCharError"
    except NeedCharError:
        return "Вызвано исключение NeedCharError"
    return hashlib.sha256(password.encode()).hexdigest()

print(password_validation(
    "$uNri$e_777",
    min_length=6,
    at_least_one=lambda char: char in "!@#$%^&*()_"
))
