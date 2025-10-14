# def solution(w):
#     l = 0
#     u = 0
#     for c in w:
#         if c.islower():
#             l += 1
#         else:
#             u += 1
#     return w.lower() if max(l, u) == l else w.upper()

# print(solution(input()))

# faster
w = input()
l = sum(c.islower() for c in w)
u = len(w) - l
print(w.lower() if l >= u else w.upper())