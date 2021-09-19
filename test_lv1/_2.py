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
