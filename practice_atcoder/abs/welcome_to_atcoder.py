def question(a, bc, s):
    exa = int(a)
    exb, exc = map(int, bc.split())
    exs = s
    return f"{exa + exb + exc} {exs}"
