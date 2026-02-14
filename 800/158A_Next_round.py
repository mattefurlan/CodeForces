def round(rules, scores):
    count = 0
    i_th = scores[rules[1] - 1]
    for n in scores:
        if n < i_th:
            return count
        if n > 0 and n >= i_th:
            count += 1
    return count


n_k = list(map(int, input().split()))
scores = list(map(int, input().split()))

print(round(n_k, scores))