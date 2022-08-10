text = input()
s = input()
sst = text[0 : int(len(text) / 2)]
if sst in s:
    print(True)
else:
    print(False)