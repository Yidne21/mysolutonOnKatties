import math
num = input()
dl = []
for i in num:
    if int(i) > 0:
        dl.insert(0, int(i))
    elif math.prod(dl) >= 10:
        num = math.prod(dl)
    elif math.prod(dl) < 10:
        print(math.prod(dl))
        break

