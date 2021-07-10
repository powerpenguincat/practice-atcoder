def question(s):
    exs = s

    # 重複しないところから変換する
    exs = exs.replace("eraser", "")
    exs = exs.replace("erase", "")
    exs = exs.replace("dreamer", "")
    exs = exs.replace("dream", "")

    return "YES" if (exs == "") else "NO"
