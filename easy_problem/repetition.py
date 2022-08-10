text = input()
l = []
sustr = text[0]
for i in text[1:]:
    if i in sustr:
        sustr += i
    elif i not in sustr:
        l.append(sustr)
        sustr = i
l.append(sustr)
if len(l) > 0:
    max = len(l[0])
    for i in l[1:]:
        if len(i) > max:
            max = len(i)
    print(max)
else:
    print(len(text))
