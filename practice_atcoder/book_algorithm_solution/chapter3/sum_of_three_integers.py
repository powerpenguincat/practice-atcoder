def question(ks):
    exk, exs = map(int, ks.split())

    cnt = 0
    for x in range(exk+1):
        for y in range(exk+1):
            for z in range(exk+1):
                if x + y + z == exs:
                    cnt += 1

    return f"{cnt}"
