# H - Напишите функцию is_palindrome, которая принимает натуральное число, строку, кортеж или список, 
# а возвращает логическое значение: True — если передан палиндром, а в противном случае — False.
def is_palindrome(value):
    if isinstance(value, int):
        # Преобразуем число в строку для упрощения проверки
        value = str(value)
    if isinstance(value, (str, tuple, list)):
        # Определяем, является ли переданное значение палиндромом
        # Для этого сравниваем его с обратным порядком элементов
        return value == value[::-1]
    else:
        # Если переданное значение не является целым числом, строкой, кортежем или списком,
        # возвращаем False
        return False
    
# I - Напишите функцию is_prime, которая принимает натуральное число, а возвращает булево значение: 
# True — если переданное число простое, а иначе — False.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# J - Напишите функцию merge, которая принимает два отсортированных по возрастанию кортежа целых чисел, 
# а возвращает один из всех переданных чисел.
def merge(tuple1, tuple2):
    result = []
    i = 0
    j = 0
    while i < len(tuple1) and j < len(tuple2):
        if tuple1[i] < tuple2[j]:
            result.append(tuple1[i])
            i += 1
        else:
            result.append(tuple2[j])
            j += 1
    result.extend(tuple1[i:])
    result.extend(tuple2[j:])
    return tuple(result)