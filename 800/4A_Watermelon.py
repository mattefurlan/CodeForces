def divide_watermelon(w):
    if w % 2 == 0 and w > 2:
        return "YES"
    return "NO"
 
w = int(input())
print(divide_watermelon(w))
