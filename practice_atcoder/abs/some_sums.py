def question(nab):
    exn, exa, exb = map(int, nab.split())

    result = 0
    for ni in range(exn + 1):
        sums = sum(map(int, list(str(ni))))
        if exa <= sums <= exb:
            result += ni

    return f"{result}"
