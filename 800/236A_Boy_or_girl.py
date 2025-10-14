'''
This is his method: if the number of distinct characters in one's user name is odd, then he is a male, otherwise she is a female. You are given the string that denotes the user name, please help our hero to determine the gender of this user by his method.

Input
The first line contains a non-empty string, that contains only lowercase English letters — the user name. This string contains at most 100 letters.

Output
If it is a female by our hero's method, print "CHAT WITH HER!" (without the quotes), otherwise, print "IGNORE HIM!" (without the quotes).
'''

# def f(w):
#     d = []
#     for c in w:
#         if c not in d:
#             d.append(c)
#     return "CHAT WITH HER!" if len(d) % 2 == 0 else "IGNORE HIM!"

# a = input()
# print(f(a))

# meglio:
def f(w):
    return "CHAT WITH HER!" if len(set(w)) % 2 == 0 else "IGNORE HIM!"

a = input()
print(f(a))

