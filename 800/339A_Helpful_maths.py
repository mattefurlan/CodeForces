

# def to_list(o):
#     l = o.split("+")
#     return sorted(l)

# def p(l):
#     for i in range(len(l)- 1):
#         print(l[i], end="+")
#     print(l[-1])

# inp1 = input()

# li = to_list(inp1)
# p(li)



# meglio:
inp1 = input()
print("+".join(sorted(inp1.split("+"))))

