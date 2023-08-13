# D - Напишите декоратор answer, который преобразует функцию, принимающую неограниченное число позиционных 
# и именованных параметров и возвращает её результат с припиской "Результат функции: <значение>".
def answer(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f'Результат функции: {result}'
    return wrapper

# E - В некоторых случаях полезно накапливать результат, а затем получать его единым списком.
# Реализуйте декоратор result_accumulator, который модернизирует функцию с неопределенным количеством 
# позиционных параметров следующим образом:
#  - Добавляет именованный параметр method со значением по умолчанию accumulate;
#  - При вызове функции с параметром method равным accumulate, результат сохраняется в очередь 
# (для каждой функции в собственную), а функция ничего не возвращает;
#  - При вызове функции с параметром method равным drop, возвращается все накопленные результаты, а очередь сбрасывается.
def result_accumulator(fn):
    def wrapper(*args, **kwargs):
        wrapper.results.append(fn(*args))
        if kwargs.get('method') == 'drop':
            res, wrapper.results = wrapper.results, []
            return res
    wrapper.results = []
    return wrapper

# F - Напишите рекурсивную функцию merge_sort, которая производит сортировку списка.
def merge_sort(arr):
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
        return result
    
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)