def question(s):
    exss = list(s)

    result = 0
    # 間に加算をいれるかいれないか
    for i in range(2**(len(exss)-1)):
        e = 0

        for j in range(len(exss)):
            result += int(exss[-(j+1)]) * (10 ** e)
            e += 1
            # 0, 10, 11, 100, 101, ... で 1 を + と見立てて加算する
            if i >> j & 1:
                e = 0

    return f"{result}"
