inp = input()
x, r = map(int, inp.split())
if x > r:
    if x - r == 1:
        print("Dr. Chaz needs {} more piece of chicken!".format(x-r))
    else:
        print("Dr. Chaz needs {} more pieces of chicken!".format(x-r))
elif r > x:
    if r - x == 1:
        print("Dr. Chaz will have {} piece of chicken left over!".format(r - x))
    else:
        print("Dr. Chaz will have {} pieces of chicken left over!".format(r - x))
