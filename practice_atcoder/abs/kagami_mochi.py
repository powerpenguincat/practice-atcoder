def question(n, dn):
    exn = int(n)
    exdn = map(int, dn)

    return f"{len(set(exdn))}"
