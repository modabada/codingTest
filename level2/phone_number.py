# https://programmers.co.kr/learn/courses/30/lessons/42577


def solution(phone_book):
    phone_book.sort()
    tmp = phone_book[0]
    for i in range(1, len(phone_book)):
        if phone_book[i][:len(tmp)] == tmp:
            return False
        tmp = phone_book[i]
    return True
