text = input()
tot = 0
for i in text:
    tot += ord(i)
print(chr(tot // len(text)))
