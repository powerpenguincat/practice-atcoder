def question(nab):
    n, a, b = map(int, nab.split())

    result = 0
    for ni in range(n + 1):
        sums = sum(map(int, list(str(ni))))
        if a <= sums <= b:
            result += ni

    return f"{result}"
