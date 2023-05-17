# A
print("Как Вас зовут?")
a = input()
print(f"Здравствуйте, {a}!")
print("Как дела?")
b = input()
if b == "хорошо":
    print("Я за вас рада!")
if b == "плохо":
    print("Всё наладится!")

# B
a = int(input())
b = int(input())
if (a > b):
    print("Петя")
else:
    print("Вася")

# C
a = int(input())
b = int(input())
c = int(input())
if (a > b and a > c):
    print("Петя")
elif (b > a and b > c):
    print("Вася")
else:
    print("Толя")

# D
name = ["Петя", "Вася", "Толя"]  # создаем список имен
# создаем список размерностью 3, заполненный пустыми строками
rang = ["", "", ""]
speed = [0, 0, 0]  # создаем список скоростей, изначально заполняем нулями
# каждому элементу в списке speed присваиваем скорость через терминал ввода
speed[0] = int(input())
speed[1] = int(input())
speed[2] = int(input())

for i in range(len(speed)):  # проходим по списку speed
    # пустые строки заполняем именем человека у которого максимальная скорость
    rang[i] = name[speed.index(max(speed))]
    # обнуляем максимум, чтобы найти снова максимум среди оставшихся
    speed[speed.index(max(speed))] = 0

for i in range(len(rang)):  # проходим по заполненному уже списку rang с именами
    print(f"{i + 1}. {rang[i]}")  # вписываем индекс и имя в порядке убывания

# или
speed1 = int(input("Введите скорость для Пети: "))
speed2 = int(input("Введите скорость для Васи: "))
speed3 = int(input("Введите скорость для Толи: "))

if speed1 >= speed2 and speed1 >= speed3:
    print("1. " + "Петя")
    if speed2 >= speed3:
        print("2. " + "Вася")
        print("3. " + "Толя")
    else:
        print("2. " + "Толя")
        print("3. " + "Вася")
elif speed2 >= speed1 and speed2 >= speed3:
    print("1. " + "Вася")
    if speed1 >= speed3:
        print("2. " + "Петя")
        print("3. " + "Толя")
    else:
        print("2. " + "Толя")
        print("3. " + "Петя")
else:
    print("1. " + "Толя")
    if speed1 >= speed2:
        print("2. " + "Петя")
        print("3. " + "Вася")
    else:
        print("2. " + "Вася")
        print("3. " + "Петя")