def solution(n, t, m, timetable):
    startTime = 9 * 60
    answer = 0
    table = sorted([(int(tb[:2]) * 60) + int(tb[3:]) for tb in timetable])
    cnt = 0

    for j in range(n):
        max_c = m;
        
        for i in range(cnt, len(table)):
            if table[i] <= startTime:
                max_c -= 1
                cnt += 1
                if max_c == 0:
                    break

        if j == (n - 1):
            # 자리없으면 1분먼저, 아니면 버스 출발시간
            answer = table[cnt - 1] - 1 if max_c == 0 else startTime
        startTime += t
        if startTime >= 60 * 24:
            break

    hour = str(answer // 60)
    if len(hour) == 1:
        hour = "0" + hour
    minute = str(answer % 60)
    if len(minute) == 1:
        minute = "0" + minute
    return hour + ":" + minute


p1 = [
    1,
    2,
    2, 
    1, 
    1,
    10
]
p2 = [
    1,
    10,
    1,
    1,
    1,
    60
]
p3 = [
    5,
    2,
    2,
    5,
    1,
    45
]
p4 = [
    ["08:00", "08:01", "08:02", "08:03"],
    ["09:10", "09:09", "08:00"],
    ["09:00", "09:00", "09:00", "09:00"],
    ["00:01", "00:01", "00:01", "00:01", "00:01"],
    ["23:59"],
    ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
]
ans = [
    "09:00",
    "09:09",
    "08:59",
    "00:00",
    "09:00",
    "18:00"
]