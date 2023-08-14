# A - Разработайте класс Point, который при инициализации принимает координаты точки на декартовой плоскости и сохраняет 
# их в поля x и y соответственно.
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(3, 5)
print(point.x, point.y)

# B - Реализуйте методы:
# move, который перемещает точку на заданное расстояние по осям x и y;
# length, который определяет до переданной точки расстояние, округлённое до сотых.
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, step_x, step_y):
        self.x += step_x
        self.y += step_y
    
    def length(self, obj):
        return round(((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5, 2)
       
point = Point(3, 5)
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)

first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))

# С - Напишите класс RedButton, который описывает красную кнопку.
# Класс должен реализовывать методы:
# click() — эмулирует нажатие кнопки, выводит сообщение "Тревога!";
# count() — возвращает количество раз, которое была нажата кнопка.
class RedButton:

    def __init__(self):
        self.attention = False
        self.cnt = 0
    
    def click(self):
        print("Тревога!")
        self.cnt += 1
    
    def count(self):
        return self.cnt  

button = RedButton()
for time in range(5):
    button.click()
print(button.count())