def tanyaSub(n, k):
    for i in range(k):
        if n % 10 == 0:
            n //= 10
        else:
            n -= 1
    return n

m = list(map(int, input().split()))
m0 = m[0]
m1 = m[1]

print(tanyaSub(m0, m1))
        