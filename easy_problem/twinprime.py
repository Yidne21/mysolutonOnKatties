import math


def is_prime(n):
    isprime = True
    for i in range(2, n):
        if n % i == 0:
            isprime = False
    return isprime

hashmap = {}
def main():
    r = 20000000
    l = []
    k = 1
    prv = 3
    for i in range(1000000, 100000):
        prv = i
        if is_prime(prv):
            nxt = prv + 2
            if is_prime(nxt):
                hashmap[k] = (prv, nxt)
                k += 1
                prv = nxt

    print(hashmap)


main()
