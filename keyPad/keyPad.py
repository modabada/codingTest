# https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3
def solution(numbers, hand):
    key = [
        1, 2, 3,
        4, 5, 6,
        7, 8, 9,
        '*', 0, '#'
    ]
    # key = [1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#']    값
    # key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]      인덱스
    # n = 4
    # key[int(n / 3)][n % 3]                            찾는 법
    # key [ 몫 ] [ 나머지 ]
    left = 9
    right = 11
    answer = []

    for e in numbers:
        if e in [1, 4, 7]:
            answer.append('L')
            left = key.index(e)
        elif e in [3, 6, 9]:
            answer.append('R')
            right = key.index(e)
        else:
            inx = key.index(e)
            left_d = abs(int(inx / 3) - int(left / 3)) + abs(inx % 3 - left % 3)
            right_d = abs(int(inx / 3) - int(right / 3)) + abs(inx % 3 - right % 3)
            if left_d < right_d:
                answer.append('L')
                left = key.index(e)
            elif left_d > right_d:
                answer.append('R')
                right = key.index(e)
            else:
                if hand == 'left':
                    answer.append('L')
                    left = key.index(e)
                else:
                    answer.append('R')
                    right = key.index(e)
    return ''.join(answer)
