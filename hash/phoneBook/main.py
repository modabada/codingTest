def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    word = list()
    for e in phone_book:
        if len(e) != phone_book[0]:
            break
        word.append(e)
    print(word)
    return answer
