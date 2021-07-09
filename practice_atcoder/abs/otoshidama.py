def question(ny):
    exn, exy = map(int, ny.split())

    results = []
    for xi in range(exn + 1):
        for yi in range(exn + 1 - xi):
            for zi in range(exn + 1 - xi - yi):
                if exy == xi * 10000 + yi * 5000 + zi * 1000:
                    return f"{xi} {yi} {zi}"

    return "-1 -1 -1"
