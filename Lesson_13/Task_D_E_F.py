# D - Рассмотрим объект «Программист», который задаётся именем, должностью и количеством отработанных часов. 
# Каждая должность имеет собственный оклад (заработную плату за час работы). В нашей импровизированной компании 
# существуют 3 должности:
# Junior — с окладом 10 тугриков в час;
# Middle — с окладом 15 тугриков в час;
# Senior — с окладом 20 тугриков в час по умолчанию и +1 тугрик за каждое новое повышение.
# Напишите класс Programmer, который инициализируется именем и должностью (отработка у нового работника равна нулю). 
# Класс реализует следующие методы:
# work(time) — отмечает новую отработку в количестве часов time;
# rise() — повышает программиста;
# info() — возвращает строку для бухгалтерии в формате: <имя> <количество отработанных часов>ч. <накопленная зарплата>тгр.
class Programmer:

    def __init__(self, name, pos, time=0):
        self.name = name
        self.pos = pos
        self.time = time
        self.salary = 10 if pos == "Junior" else 15 if pos == "Middle" else 20
        self.temp = 0

    def work(self, time):
        self.time += time
        self.temp += self.salary * time

    def rise(self):
        if self.pos == "Junior":
            self.pos = "Middle"
            self.salary += 5
        elif self.pos == "Middle":
            self.pos = "Senior"
            self.salary += 5
        elif self.pos == "Senior":
            self.salary += 1
        return self.salary

    def info(self):
        return f'{self.name} {self.time}ч. {self.temp}тгр.'

programmer = Programmer('Васильев Иван', 'Middle')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())

# E - Разработайте класс Rectangle.
# При инициализации класс принимает два кортежа рациональных координат противоположных углов прямоугольника.
# Класс должен реализовывать методы:
# perimeter — возвращает периметр прямоугольника;
# area — возвращает площадь прямоугольника.
# Все результаты вычислений нужно округлить до сотых.
class Rectangle:

    def __init__(self, first_coord, sec_coord):
        self.first_coord = first_coord
        self.sec_coord = sec_coord
    
    def perimeter(self):
        d1 = abs(self.sec_coord[0] - self.first_coord[0])
        d2 = abs(self.sec_coord[1] - self.first_coord[1])
        return round(2 * (d1 + d2), 2)

    def area(self):
        d1 = abs(self.sec_coord[0] - self.first_coord[0])
        d2 = abs(self.sec_coord[1] - self.first_coord[1])
        return round(d1 * d2, 2)


rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())
rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())

# F - Реализуйте методы:
# get_pos() — возвращает координаты верхнего левого угла в виде кортежа;
# get_size() — возвращает размеры в виде кортежа;
# move(dx, dy) — изменяет положение на заданные значения;
# resize(width, height) — изменяет размер (положение верхнего левого угла остаётся неизменным).
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.
class Rectangle:
    def __init__(self, first_coord, sec_coord):
        self.x = min(first_coord[0], sec_coord[0])
        self.y = max(first_coord[1], sec_coord[1])
        self.width = abs(first_coord[0] - sec_coord[0])
        self.height = abs(first_coord[1] - sec_coord[1])

    def perimeter(self):
        return round(2 * (self.width + self.height), 2)

    def area(self):
        return round(self.width * self.height, 2)

    def get_pos(self):
        return (round(self.x, 2), round(self.y, 2))

    def get_size(self):
        return (round(self.width, 2), round(self.height, 2))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height