inp = input()
p, min, r = map(int, inp.split())
hashmap = {}
iswin = False
for i in range(p):
    par = input()
    hashmap[par] = 0
for i in range(r):
    text = input()
    name, point = map(str, text.split())
    hashmap[name] = int(point) + hashmap.get(name)
    if hashmap.get(name) == min:
        iswin = True
        print("{} wins!".format(name))
if not iswin:
    print("No winner!")
