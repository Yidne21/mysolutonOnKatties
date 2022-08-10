n =int(input())
l = []
hashmapd = {}
hashmapk = {}
for i in range(n*2):
    s = input()
    l.append(s)
    if i < n:
        hashmapd[s] = 1 + hashmapd.get(s, 0)
    else:
        hashmapk[s] = 1 + hashmapk.get(s, 0)
d = set(l[0:n])
k = set(l[n:])
com = d.intersection(k)
sum = 0
for i in com:
    if hashmapk.get(i) < hashmapd.get(i):
        sum += hashmapk.get(i)
    else:
        sum += hashmapd.get(i)
print(sum)
