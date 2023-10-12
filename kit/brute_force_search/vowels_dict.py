# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    answer = 0
    d={'A':0,'E':1,'I':2,'O':3,'U':4}
    for i in range(len(word)):
        answer += 1 + d[word[i]] * ((5 ** (5 - i) - 1) / 4)

    return answer
