r = int(input())
l = []
for i in range(r):
    word = input()
    l.append(word)
hashmap = {}
for w in l:
    hashmap[w] = l.count(w)
min = l.count(l[0])
for i in l[1:]:
    if l.count(i) < min:
        min = l.count(i)
res = []
for k, v in hashmap.items():
    if v == min:
        res.append(k)
for i in sorted(res):
    print(i)
