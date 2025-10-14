def way_2_long(s):
    if len(s) <= 10:
        return s
    return "" + s[0] + str(len(s) -2) +s[-1]

n = int(input())
for _ in range(n):
    word = input().strip()
    print(way_2_long(word))