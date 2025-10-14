def b_b_b(a, b):
    y = 0
    while a <= b:
        a *= 3
        b *= 2
        y += 1
    return y

a, b = map(int, input().split())
print(b_b_b(a, b))
    
