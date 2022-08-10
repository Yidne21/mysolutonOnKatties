n = int(input())
hashdic = {}
for i in range(n):
    inp = input()
    inp = inp.split()
    ar = inp[0]
    am = inp[2]
    hashdic[ar] = am
try:
    while True:
        w = input()
        w = w.split()
        for i in w:
            print("{} ".format(hashdic.get(i, i)), end="")
except:
    pass
