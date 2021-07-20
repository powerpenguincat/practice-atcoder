def question(n, abcn):
    exn = int(n)
    a = 0
    b = 0
    c = 0
    for abci in abcn:
        exa, exb, exc = map(int, abci.split())
        tmpa = exa+max(b, c)
        tmpb = exb+max(a, c)
        tmpc = exc+max(a, b)
        a = tmpa
        b = tmpb
        c = tmpc

    return f"{max(a, b, c)}"
