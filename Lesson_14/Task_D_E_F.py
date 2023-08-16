"""
D - Возможно, вы уже заметили, что дробные числа (float) недостаточно точные для некоторых задач. 
Для более точных математических расчётов иногда прибегают к созданию правильных рациональных 
дробей, описываемых числителем и знаменателем.
Начнём разработку класса Fraction, который реализует предлагаемые дроби.
Предусмотрите возможность инициализации дроби с помощью двух целых чисел или строки в формате <числитель>/<знаменатель>.
В случаях наличия общего делителя у числителя и знаменателя, дробь следует сократить.
А также реализуйте методы:
numerator() — возвращает значение числителя;
numerator(number) — изменяет значение числителя и производит сокращение дроби, если это необходимо;
denominator() – возвращает значение знаменателя;
denominator(number) — изменяет значение знаменателя и производит сокращение дроби, если необходимо;
__str__ — возвращает строковое представление дроби в формате <числитель>/<знаменатель>;
__repr__ — возвращает описание объекта в формате Fraction(<числитель>, <знаменатель>).
Примечание
Будем считать, что пользователь знает о запрете деления на ноль.
Все числа в данной задаче будут положительными.
Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть с использованием 
ведущих символов нижнего подчёркивания).
"""
class Fraction:

    def __init__(self, x, y=None):
        if isinstance(x, int):
            self.x, self.y = x, y
        elif isinstance(x, str):
            x = x.split("/")
            self.x, self.y = int(x[0]), int(x[1])
        self.__result()
        self.mixed_number = self.__to_mixed()

    def numerator(self, num=None):
        if num:
            self.x = num
            self.__result()
            self.mixed_number = self.__to_mixed()
        return self.x

    def denominator(self, num=None):
        if num:
            self.y = num
            self.__result()
            self.mixed_number = self.__to_mixed()
        return self.y

    def __str__(self):
        return f'{self.x}/{self.y}'

    def __repr__(self) -> str:
        return f'Fraction({self.x}, {self.y})'

    def __gcd(self, x, y):
        while y:
            x, y = y, x % y
        return x

    def __result(self):
        common_divisor = self.__gcd(self.x, self.y)
        self.x //= common_divisor
        self.y //= common_divisor

    def __to_mixed(self):
        if self.x >= self.y:
            quotient, remainder = divmod(self.x, self.y)
            return f'{quotient} {remainder}/{self.y}'

# E - Продолжим разработку класса Fraction, который реализует предлагаемые дроби.
# Предусмотрите возможность задать отрицательные числитель и/или знаменатель. 
# А также перепишите методы __str__ и __repr__ таким образом, чтобы информация об объекте 
# согласовывалась с инициализацией строкой.
# Далее реализуйте оператор математического отрицания — унарный минус.
# Примечание
# Будем считать, что пользователь знает о запрете деления на ноль.
# Все поля и методы, не требуемые в задаче, следует инкапсулировать 
# (называть с использованием ведущих символов нижнего подчёркивания).
class Fraction:
    def __init__(self, x, y=None):
        if isinstance(x, int):
            self.x, self.y = x, y
        elif isinstance(x, str):
            x = x.split("/")
            self.x, self.y = int(x[0]), int(x[1])
        self.__result()
        self.mixed_number = self.__to_mixed()

    def numerator(self, num=None):
        if num is not None:
            self.x = num
            self.__result()
            self.mixed_number = self.__to_mixed()
        return abs(self.x)

    def denominator(self, num=None):
        if num is not None:
            self.y = num
            self.__result()
            self.mixed_number = self.__to_mixed()
        return abs(self.y)

    def __str__(self):
        return f"{self.x}/{self.y}"

    def __repr__(self) -> str:
        return f"Fraction('{self.x}/{self.y}')"

    def __gcd(self, x, y):
        while y:
            x, y = y, x % y
        return x

    def __result(self):
        common_divisor = self.__gcd(self.x, self.y)
        self.x //= common_divisor
        self.y //= common_divisor
        if self.y < 0:
            self.x = -self.x
            self.y = -self.y
        if self.x < 0 and self.y < 0:
            self.x = abs(self.x)
            self.y = abs(self.y)

    def __to_mixed(self):
        if self.x >= self.y:
            quotient = self.x // self.y
            remainder = self.x % self.y
            return f'{quotient} {remainder}/{self.y}'

    def __neg__(self):
        return Fraction(self.x, -self.y)

a = Fraction('-1/2')
b = -a
print(a, b, a is b)
b.numerator(-b.numerator())
a.denominator(-3)
print(a, b)
print(a.numerator(), a.denominator())
print(b.numerator(), b.denominator())

# F - Продолжим разработку класса Fraction, который реализует предлагаемые дроби.
# Реализуйте бинарные операторы:
# + — сложение дробей, создаёт новую дробь;
# - — вычитание дробей, создаёт новую дробь;
# += — сложение дробей, изменяет дробь, переданную слева;
# -= — вычитание дробей, изменяет дробь, переданную слева.
class Fraction:
    def __init__(self, x, y=None):
        if isinstance(x, int):
            self.x, self.y = x, y
        elif isinstance(x, str):
            x = x.split("/")
            self.x, self.y = int(x[0]), int(x[1])
        self.__result()
        self.mixed_number = self.__to_mixed()
        self.original = (self.x, self.y)

    def numerator(self, num=None):
        if num:
            self.x = num
            self.__result()
            self.mixed_number = self.__to_mixed()
        return abs(self.x)

    def denominator(self, num=None):
        if num:
            self.y = num
            self.__result()
            self.mixed_number = self.__to_mixed()
        return abs(self.y)

    def __str__(self):
        return f"{self.x}/{self.y}"

    def __repr__(self) -> str:
        return f"Fraction('{self.x}/{self.y}')"

    def __gcd(self, x, y):
        while y:
            x, y = y, x % y
        return x

    def __result(self):
        common_divisor = self.__gcd(self.x, self.y)
        self.x //= common_divisor
        self.y //= common_divisor

    def __to_mixed(self):
        if self.x >= self.y:
            quotient = self.x // self.y
            remainder = self.x % self.y
            return f'{quotient} {remainder}/{self.y}'

    def __neg__(self):
        return Fraction(self.x, -self.y)

    def __add__(self, other):
        x = self.x * other.y + other.x * self.y
        y = self.y * other.y
        return Fraction(x, y)

    def __iadd__(self, other):
        self.x = self.x * other.y + other.x * self.y
        self.y = self.y * other.y
        self.__result()
        self.mixed_number = self.__to_mixed()
        return self

    def __sub__(self, other):
        x = self.x * other.y - other.x * self.y
        y = self.y * other.y
        return Fraction(x, y)

    def __isub__(self, other):
        self.x = self.x * other.y - other.x * self.y
        self.y = self.y * other.y
        self.__result()
        self.mixed_number = self.__to_mixed()
        return self
    
a = Fraction(1, 3)
b = Fraction(1, 2)
c = a + b
print(a, b, c, a is c, b is c)      