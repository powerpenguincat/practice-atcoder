def question(a, b, c, x):
    exa = int(a)
    exb = int(b)
    exc = int(c)
    exx = int(x)

    exx_cnt = exx / 50

    cnt = 0
    for ai in range(exa + 1):
        for bi in range(exb + 1):
            for ci in range(exc + 1):
                if exx_cnt == ai * 10 + bi * 2 + ci * 1:
                    cnt += 1

    return f"{cnt}"
