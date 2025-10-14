n_s = int(input())
x = 0
plus = ["X++", "++X"]
minus = ["X--", "--X"]

for i in range(n_s):
    s = input()
    if s in plus:
        x += 1
    else:
        x -= 1

print(x)
    

