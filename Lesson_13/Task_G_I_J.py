# G - Необходимо ещё немного доработать предыдущую задачу.
# Разработайте методы:
# turn() — поворачивает прямоугольник на 90&deg; по часовой стрелке вокруг его центра;
# scale(factor) — изменяет размер в указанное количество раз, тоже относительно центра.
# Все вычисления производить с округлением до сотых.
class Rectangle:
    def __init__(self, first_coord, sec_coord):
        self.first_coord = first_coord
        self.sec_coord = sec_coord
        self.width = abs(first_coord[0] - sec_coord[0])
        self.height = abs(first_coord[1] - sec_coord[1])
        self.center = ((first_coord[0] + sec_coord[0]) / 2,
                       (first_coord[1] + sec_coord[1]) / 2)

    def get_pos(self):
        return (round(-self.first_coord[0], 2), round(self.first_coord[1], 2))

    def get_size(self):
        return (round(self.width, 2), round(self.height, 2))

    def turn(self):
        dx = self.sec_coord[0] - self.center[0]
        dy = self.sec_coord[1] - self.center[1]
        self.first_coord = (-dy + self.center[0], -dx + -self.center[1])
        self.sec_coord = (dx + self.center[0], dy + self.center[1])
        self.width, self.height = self.height, self.width
        self.center = ((self.first_coord[0] + self.sec_coord[0]) / 2,
                       (self.first_coord[1] + self.sec_coord[1]) / 2)

    def scale(self, factor):
        self.width *= factor
        self.height *= factor
        self.first_coord = (
            round(self.first_coord[0] * factor, 2), round(self.first_coord[1] * factor, 2))
        self.sec_coord = (
            self.first_coord[0] + self.width, self.first_coord[1] + self.height)
        self.center = ((self.first_coord[0] + self.sec_coord[0]) / 2,
                       (self.first_coord[1] + self.sec_coord[1]) / 2)

rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.turn()
print(rect.get_pos(), rect.get_size(), sep='\n')

# I - В программировании существует потребность не только в изученных нами коллекциях. 
# Одна из таких очередь. Она реализует подход к хранению данных по принципу «Первый вошёл – первый ушел».
# Реализуйте класс Queue, который не имеет параметров инициализации, но поддерживает методы:
# push(item) — добавить элемент в конец очереди;
# pop() — «вытащить» первый элемент из очереди;
class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop(0)
    
    def is_empty(self):
        return not bool(self.items)
    
# J - Ещё одной полезной коллекцией является стек реализующий принцип «Последний пришёл – первый ушёл». 
# Его часто представляют как стопку карт или магазин пистолета, где приходящие элементы закрывают 
# выход уже находящимся в коллекции.
# Реализуйте класс Stack, который не имеет параметров инициализации, но поддерживает методы:
# push(item) — добавить элемент в конец стека;
# pop() — «вытащить» первый элемент из стека;
# is_empty() — проверяет стек на пустоту.
class Stack:

    def __init__(self):
        self.st = []
    
    def push(self, item):
        self.st.append(item)
    
    def pop(self):
        return self.st.pop()
    
    def is_empty(self):
        return not bool(self.st)   
# По сути единственное различие от прошлой задачи в pop(0), а тут pop() без передачи доп аргумента.    