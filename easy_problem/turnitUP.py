r = int(input())
ini = 7
for i in range(r):
    req = input()
    if req == "Skru op!" and ini < 10:
        ini += 1
    elif req == "Skru ned!" and ini > 0:
        ini -= 1
print(ini)
