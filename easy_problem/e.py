t = int(input())
d1 = {}
while t:
    z = input().split()
    new_key = z[0]
    new_value = z[2]
    d1.update({new_key: new_value})
    t -= 1
try:
    while True:
        b = input()
        a = b.split()
        l = []
        for x in range(len(a)):
            if a[x] in d1:
                a[x] = d1[a[x]]
        str1 = " "
        print(str1.join(a))
except:
    pass
