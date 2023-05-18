# S - Угдать число путём деления на 2, отсекая диапазоны
a1 = 1
a2 = 1000
b = ''

while b != 'Угадал!':
    c = (a1 + a2) // 2
    print(c)
    b = input()
    if b == 'Больше':
        a1 = c + 1
    elif b == 'Меньше':
        a2 = c - 1

# T
n = int(input())
p = 0
bad = - 1
for i in range(n):
    b = int(input())
    h, r, m = b % 256, (b // 256) % 256, b // 256 ** 2
    t = ((m + r + p) * 37) % 256
    if t != h or h >= 100:
        bad = i
        break
    p = h
print(bad)        