# E
a = 7
b = 6
a1 = a - 3 + 2
b1 = b + 3 + 5 - 2
a2 = int(input())
b2 = int(input())
sum = a1 + a2
sum2 = b1 + b2
if (sum > sum2):
    print("Петя")
else:
    print("Вася")

# F - Про високосный год
a = int(input())
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0: # если год кратен 4 и не кратен 100 или кратен 400 то год високосный
    print('YES')
else:
    print('NO')    

# G - Про палиндром
str = input() 
str = str.casefold() # casefold не учитывает регистры (А, а, Б, б)
# Эта строка перевернута (1, 2, 3, 4, 5) = (5, 4 , 3, 2, 1)
rev = reversed(str)
if list(str) == list(rev):
    print("YES")
else:
    print("NO")

# Второй вариант
string = input().casefold()
print("YES" if list(string) == list(string[::-1]) else "NO")

# Третий вариант
str = input()
str = str.casefold()
length = len(str)
is_palindrome = True
for i in range(length // 2):
    if str[i] != str[length - i - 1]:
        is_palindrome = False
        break
if is_palindrome:
    print("YES")
else:
    print("NO")

# H - найти слово в тексте
txt = input()
if "зайка" in txt:
    print("YES")
else:
    print("NO")

# I - найти имя с минимальным кол-вом символов
name1 = input()
name2 = input()
name3 = input()
print(min(name1, name2, name3))