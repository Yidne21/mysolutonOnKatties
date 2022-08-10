try:
    while True:
        n = input()
        n2 = input()
        s1 = set(n)
        s2 = set(n2)
        cnt = 0
        si = s1.intersection(s2)
        print(si)
        for i in si:
            c1 = n.count(i)
            c2 = n2.count(i)
            if c1 == c2:
                cnt += c1
            elif c1 > c2:
                cnt += c2
            elif c2 > c1:
                cnt += c1
        if cnt == 1:
            print("{} letter".format(cnt))
        elif cnt > 1:
            print("{} letters".format(cnt))
        elif cnt == 0:
            print("impossible")
except:
    pass
