n = int(input())
sum = (n * (n + 1)) / 2
giv = 0
for i in range(n):
    n = int(input())
    giv += n
print(sum - giv)
