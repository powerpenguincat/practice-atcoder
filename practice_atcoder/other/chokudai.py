def question(s):
    a = [1]+[0]*8
    ans = "chokudai"

    for si in s:
        for i in range(8):
            # 任意の時点までに並びが到達できていれば加算する
            a[i+1] += a[i]*(ans[i] == si)

    return f"{a[8] % (10**9+7)}"
