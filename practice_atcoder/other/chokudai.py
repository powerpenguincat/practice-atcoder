def question(s):
    a = [1]+[0]*8
    ans = "chokudai"

    for si in s:
        for i in range(8):
            a[i+1] += a[i]*(ans[i] == si)

    return f"{a[8] % (10**9+7)}"
