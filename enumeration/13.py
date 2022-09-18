n = 2
m = 9

res = [0] * n
used = [False] * (n + 1)

def rec(idx, n, m, res, used):
    if idx == n:
        print(*res, sep='')
        return
    for v in range(1, n + 1):
        if used[v]:
            continue
        res[idx] = v
        used[v] = True
        rec(idx + 1, n, m, res)
        used[v] = False

rec(0, n, m, res)
