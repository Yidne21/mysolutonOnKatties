t, r = map(int, input().split())
d = {}
for i in range(1, t+1):
    inp = input()
    inp = inp.split()
    d[i] = inp
cl = []
for i in range(1, r+1):
    if i % 3 == 0 and i % 5 == 0:
        cl.append("fizzbuzz")
    elif i % 3 == 0:
        cl.append("fizz")
    elif i % 5 == 0:
        cl.append("buzz")
    else:
        cl.append(str(i))
for k, v in d.items():
    cnt = 0
    for i in range(len(cl)):
        if v[i] != cl[i]:
            cnt += 1
    d[k] = cnt
me = min(d.values())
for k, v in d.items():
    if v == me:
        print(k)
        break
