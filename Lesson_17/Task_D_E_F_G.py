# D - Напишите функцию discount, принимающую чек из прошлой задачи и возвращающую новый с учётом акции.
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

def discount(cheque_df):
    # Создаем копию чека, чтобы не изменять оригинальный
    cheque_df_copy = cheque_df.copy()
    # Проходим по каждой строке в чеке и применяем скидку, если количество товара больше двух
    for index, row in cheque_df_copy.iterrows():
        if row['number'] > 2:
            # Вычисляем новую стоимость с учетом скидки
            discounted_cost = row['cost'] * 0.5
            # Обновляем значение стоимости в копии DataFrame
            cheque_df_copy.at[index, 'cost'] = discounted_cost
    return cheque_df_copy  # Возвращаем копию чека

# Пример использования
products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
with_discount = discount(result)
print(result)
print(with_discount)

# E - Напишите функцию get_long, 
# принимающую серию формата первой задачи и фильтрующую её по именованному параметру min_length (по умолчанию 5).
import pandas as pd

def get_long(data, min_length=5):
    # Фильтруем серию по значениям длиннее или равным min_length
    filtered = data[data >= min_length]
    return filtered

# Пример использования
data = pd.Series([3, 5, 6, 6], ['мир', 'питон', 'привет', 'яндекс'])
filtered = get_long(data)
print(data)
print(filtered)

# F - Во всех без исключения учебных заведениях ведутся журналы успеваемости. 
# Это отличный пример данных, подлежащих обработке.
# Рассмотрим журнал летней олимпиадной школы, в которой основными предметами выступают математика, 
# физика и информатика. Данные об успеваемости представлены DataFrame со столбцами:
# name — имя;
# maths — оценка по математике;
# physics — оценка по физике;
# computer science — оценка по информатике.
# Напишите функцию best, которая фильтрует всех «ударников» в журнале.
import pandas as pd

def best(journal):
    # Фильтруем учеников, у которых все оценки выше или равны 4
    filtered = journal[(journal['maths'] >= 4) & (journal['physics'] >= 4) & (journal['computer science'] >= 4)]
    return filtered

# Пример использования
columns = ['name', 'maths', 'physics', 'computer science']
data = {
    'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
    'maths': [5, 4, 5, 2, 4],
    'physics': [4, 4, 4, 5, 5],
    'computer science': [5, 2, 5, 4, 3]
}
journal = pd.DataFrame(data, columns=columns)
filtered = best(journal)
print(journal)
print(filtered)

# G - Продолжим обрабатывать DataFrame из прошлой задачи.
# Напишите функцию need_to_work_better, которая выбирает тех, у кого есть хотя бы одна двойка.
import pandas as pd

def need_to_work_better(df):
    # Фильтруем строки, в которых есть хотя бы одна двойка
    filtered = df[(df[['maths', 'physics', 'computer science']] == 2).any(axis=1)]
    return filtered

# Пример использования
columns = ['name', 'maths', 'physics', 'computer science']
data = {
    'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
    'maths': [5, 4, 5, 2, 4],
    'physics': [4, 4, 4, 5, 5],
    'computer science': [5, 2, 5, 4, 3]
}
journal = pd.DataFrame(data, columns=columns)
filtered = need_to_work_better(journal)
print(journal)
print(filtered)