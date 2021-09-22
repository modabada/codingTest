# https://programmers.co.kr/learn/courses/30/lessons/60057#qna
def solution(x: list):
    answer = len(x)  # 답 초기값
    for i in range(1, len(x) + 1):  # 자를 문자열의 글자 수
        n = 0  # 자를 문자열 인덱스
        patton = str()  # 패턴
        compressed = list()  # 압축된 문자열
        for j in range(len(x)):  # 문자열 끝까지 순회
            if n >= len(x):  # 인덱스가 문자열의 범위 벗어나면 탈출
                break
            if patton == x[n:n + i]:  # 지금 초점이 마지막 패턴과 똑같음
                compressed[-2] += 1  # 반복된 문자열 수  ++
            else:  # 마지막 패턴과 다름
                patton = x[n:n + i]  # 패턴 등록
                compressed.append(1)  # 1 회 반복됨
                compressed.append(''.join(patton))  # 압축된 문자열에 문자 추가
            n += i  # 인덱스 증가
        for j in range(compressed.count(1)):  # 1은 생략할 것임으로 압축된 문자열의 1 모두 삭제
            compressed.remove(1)
        compressed = ''.join(map(str, compressed))  # list to str
        if answer > len(compressed):
            answer = len(compressed)  # 값 갱신
    return answer
