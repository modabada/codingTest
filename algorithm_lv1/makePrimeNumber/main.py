# https://programmers.co.kr/learn/courses/30/lessons/12977
def solution(nums: list):
    answer = 0
    # 3개의 요소를 선택하기 때문에 3중 for 문을 통해 모든 조합 구함
    for x in range(0, len(nums)):
        for y in range(x + 1, len(nums)):
            for z in range(y + 1, len(nums)):
                answer += 1     # 일단 조합의 합이 소수라 가정
                n = nums[x] + nums[y] + nums[z]     # 조합의 합
                for i in range(2, (int(n ** 0.5) + 1)):     # 약수는 대칭적임으로 n의 제곱근만큼 반복
                    if n % i == 0:  # 약수가 있음 (소수가 아님)
                        answer -= 1     # 앞에서 더한거 무효화
                        break   # 더 이상 반복 금지
    return answer
