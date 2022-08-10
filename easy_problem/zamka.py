def findsumofdigit(n):
    sum = 0
    while n:
        sum += n % 10
        n = n // 10
    return  sum

l = int(input())
d = int(input())
x = int(input())
res = []
for i in range(l, d+1):
    if findsumofdigit(i) == x:
        res.append(i)
print(res[0])
print(res[len(res) - 1])
