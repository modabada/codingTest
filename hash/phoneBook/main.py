# https://programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    # 정렬하면 우선 문자열의 앞부분이 같아질거고, 그중 긴 문자열은 뒤로갈거임
    # = 앞에있는 문자열 만이 뒤의 문자열의 접두사가 될 수 있음
    phone_book.sort()
    tmp = phone_book[0]
    for i in range(1, len(phone_book)):
        if phone_book[i][:len(tmp)] == tmp:
            return False
        tmp = phone_book[i]
    return True
