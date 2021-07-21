def question(n, pn):
    exn = int(n)
    expn = list(map(int, pn.split()))

    p = 1
    for pi in expn:
        # 加算した場合(p << pi)と加算しなかった場合pの両方のビットを立る
        p = (p << pi) | p
    # 最終的にビットが立っている個数を数える
    return f"{bin(p).count('1')}"
