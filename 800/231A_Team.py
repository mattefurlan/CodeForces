n_prob = int(input())

def is_solvable(l):
    solvable = 0
    for row in l:
        if sum(row) > 1:
            solvable += 1
    return solvable
        

l = []
for i in range(n_prob):
    l.append((input().split()))

for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][j]= int(l[i][j])

print(is_solvable(l))
        
    
     