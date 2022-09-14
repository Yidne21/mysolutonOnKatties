def squareSum(n):
    s = 0
    while n > 0:
        s += (n % 10) ** 2
        n /= 10
    return s


def isHappy(n):
    sl = fa = n
    sl = squareSum(sl)
    fa = squareSum(squareSum(fa))
    while sl != fa:
        sl = squareSum(sl)
        fa = squareSum(squareSum(fa))
    else:
        return True


t = int(input())
for i in range(t):
    x, n = map(int, input().split())
    if isHappy(n):
        print("{} {} YES".format(x, n))
    else:
        print("{} {} NO".format(x, n))
