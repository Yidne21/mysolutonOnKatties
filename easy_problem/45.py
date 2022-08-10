n = int(input())
for i in range(n):
    t = input()
    cnt = 0
    for i in t:
        if i == "D":
            break
        elif i == "U":
            cnt += 1
    print(cnt)
