# A - Давайте расширим функционал класса, написанного вами в задаче «Классная точка 2.0».
# Создайте класс PatchedPoint — наследника уже написанного вами Point.
# Требуется реализовать следующие виды инициализации нового класса:
# параметров не передано — координаты точки равны 0;
# передан один параметр — кортеж с координатами точки;
# передано два параметра — координаты точки.
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, step_x, step_y):
        self.x += step_x
        self.y += step_y

    def length(self, obj):
        return round(((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5, 2)


class PatchedPoint(Point):

    def __init__(self, *args):
        if not args:
            super().__init__(0, 0)
        elif len(args) == 1 and (isinstance(args[0], (tuple, list, set))):
            super().__init__(args[0][0], args[0][1])
        else:
            super().__init__(*args)


first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))

# B - А теперь модернизируем уже новый класс PatchedPoint. Реализуйте магические методы _str__ и _repr__.
# При преобразовании в строку точка представляется в формате (x, y).
# Репрезентация же должна возвращать строку для инициализации точки двумя параметрами.
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, step_x, step_y):
        self.x += step_x
        self.y += step_y
    
    def length(self, obj):
        return round(((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5, 2)

class PatchedPoint(Point):

    def __init__(self, *args):
        if not args:
            super().__init__(0, 0)
        elif len(args) == 1 and (isinstance(args[0], (tuple, list, set))):
            super().__init__(args[0][0], args[0][1])
        else:
            super().__init__(args[0], args[1])
    
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __repr__(self) -> str:
        return f'PatchedPoint({self.x}, {self.y})'

first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(first_point, second_point)
print(*map(repr, (first_point, second_point)))

# C - Давайте вспомним о реализованном нами методе move(x, y) и напишем ему альтернативу в виде операторов + и +=.
# При выполнении кода point + (x, y), создаётся новая точка, которая отличается от изначальной на 
# заданное кортежем расстояние по осям x и y.
# При выполнении кода point += (x, y) производится перемещение изначальной точки.
# Напомним, что сейчас мы модернизируем только класс PatchedPoint.
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, step_x, step_y):
        self.x += step_x
        self.y += step_y
    
    def length(self, obj):
        return round(((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5, 2)

class PatchedPoint(Point):

    def __init__(self, *args):
        if not args:
            super().__init__(0, 0)
        elif len(args) == 1 and (isinstance(args[0], (tuple, list, set))):
            super().__init__(args[0][0], args[0][1])
        else:
            super().__init__(args[0], args[1])
    
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __repr__(self) -> str:
        return f'PatchedPoint({self.x}, {self.y})'
    
    def __add__(self, other):
        new_point = PatchedPoint(self.x + other[0], self.y + other[1])
        return new_point
    
    def __iadd__(self, other):
        self.x += other[0]
        self.y += other[1]
        return self

point = PatchedPoint()
print(point)
new_point = point + (2, -3)
print(point, new_point, point is new_point)