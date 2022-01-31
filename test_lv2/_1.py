# 입력된 문자열이 올바른 괄호 쌍인지 확인
# ()()()() -> True, ()) -> False
# 문자열은 괄호 외에는 없음
def solution(s):
    n = 0
    for e in s:
        n = n + (1 if e == "(" else -1)
        if n < 0:
            return False
    return n == 0
