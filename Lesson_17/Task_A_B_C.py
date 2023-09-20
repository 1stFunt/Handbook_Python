# A - Напишите функцию length_stats, которая получает текст,
# а возвращает объект Series со словами в качестве индексов и их длинами в качестве значений.
# Все слова в тексте предварительно переведите в нижний регистр,
# избавьтесь от знаков препинания и цифр, а также отсортируйте в лексикографическом порядке.
import pandas as pd
import re

def length_stats(text):
    # Приводим текст к нижнему регистру
    text = text.lower()
    # Удаляем знаки препинания и цифры, оставляя только буквы и пробелы
    text = re.sub(r'[^a-zA-Zа-яА-Я\s]', '', text)
    # Разбиваем текст на слова
    words = text.split()
    # Создаем словарь для подсчета длин слов
    word_lengths = {}
    for word in words:
        if word in word_lengths:
            # Если слово уже есть в словаре, продолжаем
            continue
        word_lengths[word] = len(word)
    # Создаем объект Series из словаря
    word_lengths_series = pd.Series(word_lengths)
    # Сортируем по индексу (словам) в лексикографическом порядке
    word_lengths_series = word_lengths_series.sort_index()
    return word_lengths_series

print(length_stats('Мама мыла раму'))
print(length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.'))

# B - В этот раз продумайте функцию length_stats, которая получает текст,
# а возвращает пару объектов Series со словами в качестве индексов и их длинами в качестве значений.
# Все слова в тексте предварительно переведите в нижний регистр,
# избавьтесь от знаков препинания и цифр, а также отсортируйте в лексикографическом порядке.
import pandas as pd
import re

def length_stats(text):
    # Переводим текст в нижний регистр
    text = text.lower()
    # Удаляем знаки препинания и цифры, оставляя только буквы и пробелы
    text = re.sub(r'[^a-zA-Zа-яА-Я\s]', '', text)
    # Разбиваем текст на слова
    words = text.split()
    # Инициализируем словарь для подсчета длин слов
    word_lengths_dict = {}
    # Подсчитываем длины уникальных слов и обновляем словарь
    for word in set(words):
        word_length = len(word)
        word_lengths_dict[word] = word_length
    # Сортируем слова в лексикографическом порядке
    sorted_words = sorted(word_lengths_dict.keys())
    # Создаем Series с длинами слов
    word_lengths = pd.Series([word_lengths_dict[word] for word in sorted_words], index=sorted_words)
    # Разделяем слова на четные и нечетные длины
    odd_lengths = word_lengths[word_lengths.index.map(len) % 2 == 1]
    even_lengths = word_lengths[word_lengths.index.map(len) % 2 == 0]
    return odd_lengths, even_lengths

odd, even = length_stats(
    'Лес, опушка, странный домик. Лес, опушка и зверушка.')
print(odd)
print(even)

# C - В местном магазине решили добавить анализ данных и каждый чек представлять в виде DataFrame.
# Прайс-лист уже сформирован в виде объекта Series, где индексами являются названия, а значениями — цены.
# Напишите функцию, cheque, которая принимает прайс-лист
# и список покупок в виде неопределённого количества именованных параметров (ключ — название товара, значение — количество).
# Функция должна вернуть объект DataFrame со столбцами:
# наименование продукта (product);
# цена за единицу (price);
# количество (number);
# итоговая цена (cost).
# Строки чека должны быть отсортированы по названию продуктов в лексикографическом порядке.
import pandas as pd

def cheque(price_list, **purchases):
    # Создаем списки для данных чека
    products = []
    prices = []
    quantities = []
    costs = []
    # Проходим по каждому продукту в покупках
    for product, quantity in purchases.items():
        # Проверяем, есть ли продукт в прайс-листе
        if product in price_list.index:
            price = price_list[product]
            # Вычисляем общую стоимость
            cost = price * quantity
            # Добавляем данные в списки
            products.append(product)
            prices.append(price)
            quantities.append(quantity)
            costs.append(cost)
    # Создаем DataFrame из списков
    df = pd.DataFrame({
        'product': products,
        'price': prices,
        'number': quantities,
        'cost': costs
    })
    # Сортируем строки по наименованию продукта
    df.sort_values(by='product', inplace=True)
    # Сбрасываем индексы и переназначаем их в правильном порядке
    df.reset_index(drop=True, inplace=True)
    return df

products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
print(result)