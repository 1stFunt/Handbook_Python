# S - Калькулятор обратной польской нотации (ОПН)
def rpn(a):
    s = []
    for x in a:
        if (x == '+'): 
            a2 = s[0] # присваиваем значение первого элемента к a2
            a1 = s[1] # а второго к a1, т.е. в обратном порядке
            r = int(a1) + int(a2) # получаем сумму
            s = [r] + s[2:] # сумма + все элементы начиная с третьего записываются в список s
        elif (x == '-'):
            a2 = s[0]
            a1 = s[1]
            r = int(a1) - int(a2)
            s = [r] + s[2:]
        elif (x == '*'):
            a2 = s[0]
            a1 = s[1]
            r = int(a1) * int(a2)
            s = [r] + s[2:]
        elif (x == '/'):
            a2 = s[0]
            a1 = s[1]
            r = int(a1) // int(a2)
            s = [r] + s[2:]
        else:
            s = [x] + s
    return s[0]


aa = input()
res = rpn(aa.split())
print(res)

# T - Польский калькулятор 2.0
polskiu = [] # создаем пустой список

 
def fac(n): # рекурсивная функция факториала
    if n == 0:
        return 1
    return fac(n - 1) * n
 
 
s = input().split() # вводим строку
for x in s: 
    if x == '+': # если x это +
        g = polskiu.pop() # из списка возвращаем последний элемент, а в списке удаляем его
        z = polskiu.pop() # делаем то же самое с переменной z
        polskiu.append(g + z) # суммируем значения
    elif x == '-':
        g = polskiu.pop()
        z = polskiu.pop()
        polskiu.append(z - g)
    elif x == '*':
        g = polskiu.pop()
        z = polskiu.pop()
        polskiu.append(g * z)
    elif x == '#':
        polskiu.append(polskiu[-1]) # возвращаем значение последнего элемента повторно
    elif x == '@':
        polskiu.append(polskiu[-2])
        polskiu.append(polskiu[-2])
        polskiu.append(polskiu[-5])
        del polskiu[-4]
        del polskiu[-4]
        del polskiu[-4]
    elif x == '/':
        g = polskiu.pop()
        z = polskiu.pop()
        polskiu.append(z // g)
    elif x == '~':
        g = polskiu.pop()
        polskiu.append(-g) 
    elif x == '!':
        g = polskiu.pop()
        polskiu.append(fac(g))
    else:
        polskiu.append(int(x))
print(polskiu[0]) # после всех операций выводим число, которое получилось