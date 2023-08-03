# D - Разработайте функцию month, которая возвращает название заданного месяца с заглавной буквы. 
# Функция должна принимать номер месяца и дополнительно обозначение языка (по умолчанию "ru").
def month(num, language="ru"):
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
    
# E - Напишите функцию to_string, которая формирует из последовательности данных строку.
# Функция должна принимать:
# неопределённое количество данных;
# необязательный параметр sep (по умолчанию пробел);
# необязательный параметр end (по умолчанию \n).
def to_string(*args, sep=" ", end="\n"):
    return sep.join([str(arg) for arg in args]) + end

# F - Руководство местной кофейни для программистов под названием Java-0x00 решило модернизировать систему заказа кофе.
# Для этого им требуется реализовать функцию order, которая принимает список предпочтений посетителя в 
# порядке «убывания желания».
# Согласно положению, каждый напиток в кофейне строго определён рецептом:
# Эспрессо готовится из: 1 порции кофейных зерен.
# Капучино готовится из: 1 порции кофейных зерен и 3 порций молока.
# Макиато готовится из: 2 порций кофейных зерен и 1 порции молока.
# Кофе по-венски готовится из: 1 порции кофейных зерен и 2 порций взбитых сливок.
# Латте Макиато готовится из: 1 порции кофейных зерен, 2 порций молока и 1 порции взбитых сливок.
# Кон Панна готовится из: 1 порции кофейных зерен и 1 порции взбитых сливок.
# В глобальной переменной in_stock содержится словарь, описывающий ингредиенты в наличии. 
# Ключи словаря: coffee, cream, milk.
# Функция должна вернуть:
# название напитка, который будет приготовлен;
# сообщение «К сожалению, не можем предложить Вам напиток», если ни одно из предпочтений не может быть приготовлено.
# Если заказ, может быть совершён, количество доступных ингредиентов должно соответствующим образом уменьшиться.
def order(*preferences):
    temp = "К сожалению, не можем предложить Вам напиток"
    for coffee in preferences:
        if coffee not in result or any([c in result for c in preferences]):
            if coffee == "Эспрессо" and in_stock["coffee"] > 0:
                in_stock["coffee"] -= 1
                result.append(coffee)
                temp = coffee
                break
            elif coffee == "Капучино" and in_stock['coffee'] > 0 and in_stock['milk'] > 2:
                in_stock['coffee'] -= 1
                in_stock['milk'] -= 3
                result.append(coffee)
                temp = coffee
                break
            elif coffee == "Макиато" and in_stock["coffee"] > 1 and in_stock["milk"] > 0:
                in_stock["coffee"] -= 2
                in_stock["milk"] -= 1
                result.append(coffee)
                temp = coffee
                break
            elif coffee == "Кофе по-венски" and in_stock["coffee"] > 0 and in_stock["cream"] > 1:
                in_stock["coffee"] -= 1
                in_stock["cream"] -= 2
                result.append(coffee)
                temp = coffee
                break
            elif coffee == "Латте Макиато" and in_stock["coffee"] > 0 and in_stock["milk"] > 1:
                if in_stock["cream"] > 0:
                    in_stock["coffee"] -= 1
                    in_stock["milk"] -= 2
                    in_stock["cream"] -= 1
                    result.append(coffee)
                    temp = coffee
                    break
            elif coffee == "Кон Панна" and in_stock["coffee"] > 0 and in_stock["cream"] > 0:
                in_stock["coffee"] -= 1
                in_stock["cream"] -= 1
                result.append(coffee)
                temp = coffee
                break
    if len(result) == 6 or all([c in result for c in preferences]):
        result.clear()
    return temp


result = []

in_stock = {"coffee": 1, "milk": 2, "cream": 3}