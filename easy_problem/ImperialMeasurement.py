inp = input()
inp = inp.split()
num = int(inp[0])
v = inp[1]
u = inp[3]
ul = ["thou", "inch", "foot", "yard", "chain", "furlong", "mile", "league"]
uls = ["th", "in", "ft", "yd", "ch", "fur", "mi",  "lea"]
cl = [1, 1000, 12, 3, 22, 10, 8, 3]
indv = 8
indu = 8
if v in ul:
    indv = ul.index(v)
else:
    indv = uls.index(v)

if u in ul:
    indu = ul.index(u)
else:
    indu = uls.index(u)
if indv > indu:
    for i in cl[indu+1:indv+1]:
        num *= i
    print(num)
elif indu > indv:
    for i in cl[indv + 1: indu + 1]:
        num /= i
    print(num)
