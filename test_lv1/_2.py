# 2016년 1월 1일은 금요일이다, a에 월, b에 일이 입력되고, 입력받은 날짜의 요일을 출력
# 2016년은 윤년이며, 존재할 수 없는 월은 입력되지 않는다 (ex: 13월 53일)
def solution(a, b):
    answer = 0
    arr = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(0, a - 1):
        answer += arr[i]
    answer += b
    answer = answer % 7
    if answer == 0:
        answer = "THU"
    elif answer == 1:
        answer = "FRI"
    elif answer == 2:
        answer = "SAT"
    elif answer == 3:
        answer = "SUN"
    elif answer == 4:
        answer = "MON"
    elif answer == 5:
        answer = "TUE"
    elif answer == 6:
        answer = "WED"
    return answer
