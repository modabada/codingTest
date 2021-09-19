# 로또
# https://programmers.co.kr/learn/courses/30/lessons/77484
# 로또 숫자가 일부 지워진(0) 상태에서 해당 숫자들의 조합으로 가능한 가장 높은 순위와 낮은순위 찾기
# lottos 에 지워진 로또가 있고, win_nums 에 이번 로또 숫자가 있다
def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    intersection = len(set(lottos) & set(win_nums))
    return rank[intersection + lottos.count(0)], rank[intersection]
