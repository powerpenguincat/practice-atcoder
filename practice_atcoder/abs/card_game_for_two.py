def question(n, an):
    _ = int(n)
    exan = map(int, an.split())

    sorted_exan = reversed(sorted(exan))

    alice = 0
    bob = 0
    for i, ai in enumerate(sorted_exan):
        if i % 2 == 0:
            alice += ai
        else:
            bob += ai

    return f"{alice - bob}"
