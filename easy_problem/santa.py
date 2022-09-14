import math

x, y = map(int, input().split())
if y <= 180:
    print("safe")
elif y <= 270:
    ang = 270-y
    v = math.radians(ang)
    print(int(x//math.cos(v)))
elif y>270:
    ang = y-270
    v = math.radians(ang)
    print(int(x//math.cos(v)))
