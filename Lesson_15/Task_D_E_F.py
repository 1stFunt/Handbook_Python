# D - Контроль параметров
# Напишите функцию only_positive_even_sum, которая принимает два параметра и возвращает их сумму.
# Если один из параметров не является целым числом, то следует вызвать исключение TypeError.
# Если один из параметров не является положительным чётным числом, то следует вызвать исключение ValueError.
def only_positive_even_sum(fstarg, scarg):
    try:
        if not isinstance(fstarg, int) or not isinstance(scarg, int):
            raise TypeError
        if not (fstarg > 0 and fstarg % 2 == 0) or not (scarg > 0 and scarg % 2 == 0):
            raise ValueError
    except TypeError:
        return "Вызвано исключение TypeError"
    except ValueError:
        return "Вызвано исключение ValueError"
    return fstarg + scarg

print(only_positive_even_sum("3", 2.5))

# или
def only_positive_even_sum(num1, num2):
    try:
        if not (isinstance(num1, int) and isinstance(num2, int)):
            raise TypeError("Вызвано исключение TypeError")
        if num1 <= 0 or num2 <= 0 or num1 % 2 != 0 or num2 % 2 != 0:
            raise ValueError("Вызвано исключение ValueError")
        return num1 + num2
    except (TypeError, ValueError) as e:
        return str(e) # или просто return e
    
print(only_positive_even_sum("3", 2.5))    
    
# E - Введём систему проверок:
# если один из параметров не является итерируемым объектом, то вызовите исключение StopIteration;
# если значения входных параметров содержат «неоднородные» данные, то вызовите исключение TypeError;
# если один из параметров не отсортирован, то вызовите исключение ValueError.
# Проверки следует проводить в указанном порядке.
# Если параметры прошли все проверки, верните итерируемый объект, являющийся слиянием двух переданных.
def merge(iterable1, iterable2):
    try:
        if not hasattr(iterable1, '__iter__') or not hasattr(iterable2, '__iter__'):
            raise StopIteration("Вызвано исключение StopIteration")
        if not all(isinstance(item, type(iterable1[0])) for item in iterable1) or not all(isinstance(item, type(iterable2[0])) for item in iterable2):
            raise TypeError("Вызвано исключение TypeError")
        if iterable1 != sorted(iterable1) or iterable2 != sorted(iterable2):
            raise ValueError("Вызвано исключение ValueError")
        result = []
        i, j = 0, 0
        while i < len(iterable1) and j < len(iterable2):
            if iterable1[i] < iterable2[j]:
                result.append(iterable1[i])
                i += 1
            else:
                result.append(iterable2[j])
                j += 1
        result.extend(iterable1[i:])
        result.extend(iterable2[j:])
        return result
    except (StopIteration, TypeError, ValueError) as e:
        exception_list = [str(e)]
        return exception_list

print(*merge([3, 2, 1], range(10)))

# F - В одной из первых лекций вы уже решали задачу о поиске корней квадратного уравнения. Давайте модернизируем её.
# Напишите функцию find_roots, принимающую три параметра: коэффициенты уравнения и возвращающую его 
# корни в виде кортежа из двух значений.
# Так же создайте два собственных исключения NoSolutionsError и InfiniteSolutionsError, которые будут 
# вызваны в случае отсутствия и бесконечного количества решений уравнения соответственно.
# Если переданные коэффициенты не являются рациональными числами, вызовите исключение TypeError.
class NoSolutionsError(Exception):
    pass

class InfiniteSolutionsError(Exception):
    pass

def find_roots(a, b, c):
    try:
        x1 = float(0.00)
        x2 = float(0.00)
        if a == 0 and b == 0 and c == 0:
            raise InfiniteSolutionsError
        elif a == 0 and b != 0 and c != 0:
            x1 = -(c / b)   
            return x1 
        elif a == 0 and b == 0 and c != 0:
            raise NoSolutionsError
        elif a == 0 and b != 0 and c == 0:
            x1 = 0
            return x1
        else:
            disc = (b ** 2) - (4 * a * c)
            if disc == 0:
                return (-b / (2 * a), -b / (2 * a))
            elif disc > 0:
                x1 = (-b - (disc ** 0.5)) / (2 * a)
                x2 = (-b + (disc ** 0.5)) / (2 * a)
                return min(x1, x2), max(x1, x2)
            elif disc < 0:
                raise NoSolutionsError
    except TypeError:
        return "Вызвано исключение TypeError"
    except NoSolutionsError:
        return "Вызвано исключение NoSolutionsError"
    except InfiniteSolutionsError:
        return "Вызвано исключение InfiniteSolutionsError"

print(find_roots(1, 2, 1))