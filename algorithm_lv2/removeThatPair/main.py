def solution(s):
    s = list(s)
    while True:
        inx = []
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                inx.append(i - 1)
                inx.append(i)
                break
        if not s:
            return 1
        if not inx:
            return 0
        s = [s[i] for i in range(0, len(s)) if i not in inx]
