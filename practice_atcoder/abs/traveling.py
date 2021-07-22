def question(n, txyn):
    exn = int(n)
    exts = [0 for _ in range(exn+1)]
    exxs = [0 for _ in range(exn+1)]
    exys = [0 for _ in range(exn+1)]
    for i, txyi in enumerate(txyn):
        ext, exx, exy = map(int, txyi.split())
        exts[i+1] = ext
        exxs[i+1] = exx
        exys[i+1] = exy

    can = True
    for i in range(exn):
        # 制限時間を求める
        dt = exts[i+1] - exts[i]
        # 距離を求める
        dist = abs(exxs[i+1] - exxs[i]) + abs(exys[i+1] - exys[i])
        # 制限時間内にたどりつけない場合
        if dt < dist:
            can = False
        # 行ったり来たりして時間を稼げない場合
        if dist % 2 != dt % 2:
            can = False

    return "Yes" if can else "No"
