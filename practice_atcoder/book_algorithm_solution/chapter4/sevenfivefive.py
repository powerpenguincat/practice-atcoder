def question(n):
    def fun(s):
        m = '3' in s and '5' in s and '7' in s
        # 桁数が少ない場合
        if len(s) < len(n):
            return fun(s+'3') + fun(s+'5') + fun(s+'7') + m
        # 桁数が同じで指定した数値より低い場合
        elif s <= n:
            return m
        else:
            return 0

    # 3, 5, 7, 33...
    return f"{fun('')}"
