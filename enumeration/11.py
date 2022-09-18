n = 2
m = 9

res = [0] * n
def rec(idx, n, m, res):
    if idx == n:
        print(*res, sep='')
        return
    for v in range(1, m + 1):
        res[idx] = v
        rec(idx + 1, n, m, res)

rec(0, n, m, res)
