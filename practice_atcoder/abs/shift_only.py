def question(n, an):
    _ = n
    exan = map(int, an.split())

    results = []
    for ai in exan:
        cnt = 0
        while ai % 2 == 0:
            ai = ai / 2
            cnt += 1
        results.append(cnt)

    return f"{min(results)}"
