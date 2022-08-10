inp = input()
l, h = map(int, inp.split())
winner = ""
if l * h % 2 == 0:
    winner = "Alf"
else:
    winner = "Beata"
print(winner)
