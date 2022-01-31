# https://programmers.co.kr/learn/courses/30/lessons/72410
import re


def solution(new_id):
    # 1단계
    answer = new_id.lower()

    # 2단계
    answer = ''.join([e.group() for e in re.finditer(r'[a-z\-_\d.]+', answer)])

    # 3단계
    answer = ''.join([e.group() for e in re.finditer(r'[a-z\-_\d]+|\.(?!\.)+', answer)])

    # 4단계
    if answer.startswith('.'):
        answer = answer[1:]
    if answer.endswith('.'):
        answer = answer[:-1]

    # 5단계
    if answer == '':
        answer = 'a'

    # 6단계
    elif len(answer) > 15:
        answer = answer[:15]
    if answer.endswith('.'):
        answer = answer[:-1]
    
    # 7단계
    if len(answer) < 3:
        word = list()
        word.append(answer)
        word.append(answer[-1] * (3 - len(answer)))
        answer = ''.join(word)
    return answer
