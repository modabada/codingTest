def solution(s):
    stack = list(s[:1])
    for e in s[1:]:
        if stack and stack[-1] == e:
            stack.pop()
        else:
            stack.append(e)
    return 1 if not stack else 0
