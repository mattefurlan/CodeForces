
def solve(l):
    cost = sum([l[0]*i for i in range(1, l[2] + 1)])
    if l[1] >= cost:
        return 0
    return cost - l[1]

l = list(map(int, input().split()))
print(solve(l))

