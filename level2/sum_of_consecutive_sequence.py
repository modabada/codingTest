# https://school.programmers.co.kr/learn/courses/30/lessons/178870


def solution(sequence, k):
    total = 0
    start = 0
    end = 0
    st_record = 0
    isAddedLast = False
    sq_len = len(sequence)
    while start < len(sequence):
        if not isAddedLast:
            s = sequence[end]
            total += s
        elif total <= k:
            break
        # print(start, end, sq_len, total)
        if k < total:
            total -= sequence[start] + s
            start += 1
            continue
            
        if k == total:
            l = end - start
            if l < sq_len:
                # print('updated!', sq_len, 'to', l)
                sq_len = l
                st_record = start
        if end + 1 < len(sequence):
            end += 1
        else:
            isAddedLast = True
    return [st_record, sq_len + st_record]
