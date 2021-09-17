# 로또
def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    intersection = len(set(lottos) & set(win_nums))
    return rank[intersection + lottos.count(0)], rank[intersection]
