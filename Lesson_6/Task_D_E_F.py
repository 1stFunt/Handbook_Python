# D - Количество учеников, которые любят обе каши.
# Если таких не окажется, в строке вывода нужно написать «Таких нет».
N = int(input())
M = int(input())
result = [] 
counter = 0 
for i in range(N): 
    secondname = input()  
    result.append(secondname) 
for i in range(M): 
    secondname = input() 
    if secondname not in result: 
        result.append(secondname) 
    else:
        counter += 1 
print(counter if counter > 0 else "Таких нет")

# E - Кашееды 2.0 (Количество учеников, которые любят только одну кашу).
N = int(input())
M = int(input())
result = list()
counter = 0
for i in range(N + M):
    secondname = input()
    if secondname not in result:
        result.append(secondname)
        counter += 1
    else:
        counter -= 1
print(counter if counter > 0 else "Таких нет")

# F - Кашееды — 3.0 (В алфавитном порядке фамилии учеников, которые любят только одну кашу)
N = int(input())
M = int(input())
set_1 = set()
for i in range(N + M):
    secondname = input()
    if secondname not in set_1:
        set_1.add(secondname)
    else:
        set_1.remove(secondname)
if len(set_1) > 0:
    for x in sorted(set_1):
        print(x)
else:
    print("Таких нет")