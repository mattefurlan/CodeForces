def p(x):
    if x%5 == 0:
        return x//5
    return x//5 + 1
print(p(int(input())))
