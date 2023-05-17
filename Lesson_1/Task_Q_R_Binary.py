# Q and R
number = int(input())
binary = input()
temp = 0
for i in range(len(binary)):
    temp += int(binary[i]) * 2 ** (len(binary) - i - 1) # из двоичной в десятичную
sum = number + temp
print(sum)

# или
number = int(input())
binary = input()
temp = 0
for n in binary: 
    temp = temp * 2 + int(n)
sum = number + temp 
print(sum)

# или
number = int(input())
binary = input()
temp = int(binary, 2)
sum = number + temp 
print(sum)