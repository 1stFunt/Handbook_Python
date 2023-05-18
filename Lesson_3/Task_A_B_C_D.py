# A
n = input()
while n != "Три!":
    print("Режим ожидания...")
    n = input()
print("Ёлочка, гори!")
# или
while (input()) != "Три!":
    print("Режим ожидания...")
print("Ёлочка, гори!")

# B
txt = input()
count = 0
while txt != "Приехали!":
    if "зайка" in txt:
        count += 1
    txt = input()
print(count)

# C
n1 = int(input())
n2 = int(input())
for i in range(n1, n2 + 1):
    print(f"{i}", end=" ")

# D
number1 = int(input())
number2 = int(input())
if number1 > number2:
    for i in range(number1, number2 - 1, -1):
        print(f"{i}", end=" ")
else:
    for i in range(number1, number2 + 1, +1):
        print(f"{i}", end=" ")