def su(t):
    s = 0
    for i in t:
        s += int(i)
    return s


try:
    while True:
        n = input()
        if n != "":
            s = su(n)
            r = 31 - s
            c = n.count(str(r))
            if len(n) % 2 == 0:
                if r == 0 or c == 4:
                    print("{} B".format(n))
                elif c < 4:
                    print("{} A".format(n))
            elif len(n) % 2 != 0:
                if r == 0 or c == 4:
                    print("{} A".format(n))
                elif c < 4:
                    print("{} B".format(n))
except:
    pass
