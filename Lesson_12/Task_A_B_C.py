# A - Напишите функцию recursive_sum, которая находит сумму всех позиционных аргументов.
def recursive_sum(*args):
    if len(args) == 0:
        return 0
    elif len(args) == 1:
        return args[0]
    else:
        return args[0] + recursive_sum(*args[1:])

result = recursive_sum(7, 1, 3, 2, 10)
print(result)

# B - Напишите функцию recursive_digit_sum, которая находит сумму всех цифр натурального числа.
# 1 вариант
def recursive_digit_sum(number):
    if len(str(number)) == 1:
        return int(str(number)[0])
    else:
        return int(str(number)[0]) + int(recursive_digit_sum(str(number)[1:]))
# 2 вариант
def recursive_digit_sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + recursive_digit_sum(n // 10)
        
result = recursive_digit_sum(7321346)
print(result)

# C - Напишите функцию make_equation, которая по заданным коэффициентам строит строку, описывающую 
# валидное с точки зрения Python выражение без использования оператора возведения в степень.
def make_equation(*coefs):
    if len(coefs) == 1:
        return str(coefs[0])
    else:
        return '(' + make_equation(*coefs[:-1]) + ') * x + ' + str(coefs[-1])
    
result = make_equation(3, 2, 1)
print(result)    