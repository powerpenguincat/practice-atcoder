def question(ab):
    exa, exb = map(int, ab.split())

    return "Odd" if exa * exb % 2 == 1 else "Even"

