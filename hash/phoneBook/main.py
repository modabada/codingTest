def solution(phone_book):
    phone_book.sort()
    # 정렬할 경우 앞 문자가 똑같아질거고 길이가 긴 문자는 뒤로갈것임
    # 이하 뜯어고쳐
    phone_book.sort(key=len)
    word = list()
    for e in phone_book:
        if len(e) != len(phone_book[0]):
            break
        word.append(e)
        phone_book.remove(e)
    for w in word:
        word_len = len(w)
        for e in phone_book:
            if w == e[:word_len]:
                return False
    return True
