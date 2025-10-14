def h_l(a, b):
    if a == b:
        return 0
    return s_to_ord(a, b)
     
def s_to_ord(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return 1
        elif a[i] < b[i]: 
            return -1
        else: continue
        

a = input().lower()
b = input().lower()

print(h_l(a, b))

# or return 1 if a > b else -1