def trans_sec(line):
    _, time, sec = line.split()
    h, m ,s = map(float, time.split(":"))
    sec = float(sec[:-1])
    now_end_time = (int(h)*3600 + int(m)*60)*1000 + int(s*1000)
    now_start_time = now_end_time - int(sec*1000) + 1
    return now_end_time, now_start_time

def solution(lines):
    
    answer = 0

    now_level = 0
    end_q = []
    start = []
    for line in lines:
        now_end_time, now_start_time = trans_sec(line)
        end_q.append(now_end_time)
        start.append(now_start_time)
    start.sort()
    while end_q and start:
        end = end_q[0]
        if start[0] - end_q[0] > 999:
            end_q.pop(0)
            now_level -= 1
        else:
            start.pop(0)
            now_level += 1
        
        if now_level > answer:
            answer = now_level
          
    return answer

lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
# lines = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]

print(solution(lines))
