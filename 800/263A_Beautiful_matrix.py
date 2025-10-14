# def swap_rows(matrix, i, j):
#     matrix[i], matrix[j] = matrix[j], matrix[i]
#     return matrix

# def swap_columns(matrix, i, j):
#     for row in matrix:
#         row[i], row[j] = row[j], row[i]
#     return matrix

# matrix = []
# for i in range(5):
#     matrix.append(list(map(int, input().split())))

# def find_p(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == 1:
#                return (i, j)

# p = find_p(matrix)

# count = 0

# while p[0] != 2:
#     if p[0] > 2:
#         swap_rows(matrix, p[0], p[0] - 1)
#         p = find_p(matrix)
#         count += 1
#     elif p[0] < 2:
#         swap_rows(matrix, p[0], p[0] + 1)
#         p = find_p(matrix)
#         count += 1

# while p[1] != 2:
#     if p[1] > 2:
#         swap_columns(matrix, p[1], p[1] - 1)
#         p = find_p(matrix)
#         count += 1
#     elif p[1] < 2:
#         swap_columns(matrix, p[1], p[1] + 1)
#         p = find_p(matrix)
#         count += 1
        
# print(count)


# a quanto pare non era richiesto lo swap effettivo delle colonne, ma solo i passi lol
matrix = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            print(abs(i - 2) + abs(j - 2))