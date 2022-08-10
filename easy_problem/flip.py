num = input()
num = num.split()
a = num[0]
b = num[1]
if int(a[::-1]) > int(b[::-1]):
    print(a[::-1])
else:
    print(b[::-1])