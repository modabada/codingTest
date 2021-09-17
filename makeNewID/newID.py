import re


def solution(new_id):
    answer = new_id.lower()  # 1단계
    answer = "".join([e.group() for e in re.finditer(r'([a-z\-_\d](\.?))+', answer)])  # 2, 3단계
    return answer  # "".join(answer)


r"""
작업중인 정규식
[a-z\-_\d]+|(\.(?=\.))(?!\.)+
"""
