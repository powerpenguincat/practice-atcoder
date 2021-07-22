def question(n, dn):
    _ = int(n)
    exdn = map(int, dn)

    return f"{len(set(exdn))}"
