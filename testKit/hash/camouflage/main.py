# https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3
def solution(clothes):
    answer = 1
    cloth_dict = dict()
    for e in clothes:
        if e[1] in cloth_dict:
            cloth_dict[e[1]].add(e[0])
        else:
            cloth_dict[e[1]] = {e[0]}
    # 공식: (첫번째자리의 경우의 수) * (두번째자리의 경우의 수...) - 1
    # 유도: 각 자리는 순서와 상관 없으니까 모두 곱하면 가능한 경우의 수가 나온다
    # 각 자리의 경우의 수는 (해당 부위의 옷 개수 + 1 <- 해당 부위를 입지 않은 경우)
    # 위의 식만으로는 모든 옷을 입지 않은 경우가 생김으로 모든 옷을 입지 않은 경우의 수를 제한다
    # 정의는 알고있다만 응용은 아직 많이 힘드네
    while cloth_dict:
        answer *= len(cloth_dict.popitem()[1]) + 1
    answer -= 1
    return answer
