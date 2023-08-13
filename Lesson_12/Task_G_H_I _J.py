# G - Разработайте декоратор same_type, который производит проверку переменного количества позиционных параметров.
# В случае получения не одинаковых типов выводит сообщение "Обнаружены различные типы данных" и прерывает
# выполнение функции.
def same_type(fn):
    def wrapper(*args):
        types = set(map(type, args))
        if len(types) == 1:
            return fn(*args)
        else:
            return "Обнаружены различные типы данных\nFail"
    return wrapper

# H - Напишите генератор fibonacci, который последовательно возвращает заданное количество чисел Фибоначчи
def fibonacci(n, a=0, b=1):
    if n == 0:
        return
    yield a
    yield from fibonacci(n - 1, b, a + b)

print(*fibonacci(6))

# I - Напишите генератор cycle, который принимает список и работает аналогично итератору itertools.cycle.
def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element
# или
def cycle(iterable):
    while True:
        for element in iterable:
            yield element

print(*(x for _, x in zip(range(15), cycle([1, 2, 3, 4]))))

# J - Напишите функцию make_linear, которая принимает список списков и возвращает его "выпрямленное" представление.
def make_linear(args):
    result = []
    for i in args:
        if isinstance(i, list):
            result.extend(make_linear(i))
        else:
            result.append(i)
    return result