# A - Вывести все символы этой строки без повторений.
set_1 = set(input()) 
for i in set_1: 
    print(i, end="")

# B - Вывести общие символы двух строк без повторений.    
str1 = set(input()) 
str2 = set(input()) 
str_intersection = str1 & str2  # & или str1.intersection(str2)
for i in str_intersection: 
    print(i, end="") 

# C - Вывести все найденные объекты в придорожных местностях.
n = int(input()) 
set_1 = set() 
for i in range(n): 
    string = input().split(" ") 
    for j in string: 
        set_1.add(j) 
for k in set_1: 
    print(k)     