n=input()
l=input()
x, y = map(int, n.split())
n, k = map(int, l.split())

if  n>100 or k>100 or n<0 or k<0:
    print("impossible")

z=(n*x)-(k*y)
print(z/(x-y))