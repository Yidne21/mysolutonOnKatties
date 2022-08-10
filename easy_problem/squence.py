try:
    while True:
        c = input()
        C = c.upper()
        w = input()
        w = w.split()
        res = []
        cnt = 0
        ucnt = 0
        re = ""
        for i in w:
            for h in i:
                if h in c+C:
                    re += h
                    cnt += 1
        for i in res:
            print(i, end=" ")
        print(end="\n")
except:
    pass
