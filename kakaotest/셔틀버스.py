def solution(n, t, m, timetable):
    timetable.sort()
    time_list = []
    for i in range(n):
        q , r = divmod(540 + i * t,60)
        time_list.append(str(q).rjust(2,'0') + ':' + str(r).rjust(2,'0'))
    print(time_list)
    member_list = []
    for _ in range(n):
        member_list.append([])
    idx,time_table_idx = 0, 0
    for time in timetable:
        time_table_idx += 1
        if time <= time_list[-1] and len(member_list[-1]) < m:
            if time <= time_list[idx] and len(member_list[idx]) < m:
                member_list[idx].append(time)
            elif time > time_list[idx]:
                while True:
                    idx += 1
                    if time <= time_list[idx]:
                        member_list[idx].append(time)
                        break
            else:
                idx += 1
                member_list[idx].append(time)                    
        else:
            break
    print(member_list)
    if len(member_list[-1]) < m:
        return time_list[-1]
    else:
        hour, minuate = map(int, member_list[-1][-1].split(':'))
        q, r = divmod(hour * 60 + minuate - 1, 60)
        return str(q).rjust(2,'0') + ':' + str(r).rjust(2,'0')


# print(solution(1,1,5,['08:00','08:01','08:02','08:03']))
# print(solution(2, 1, 2, ['09:00','09:00','09:00','09:00','09:00','08:00','08:01','08:02','08:03','09:03','19:13']))
print(solution(2,1,2,['09:00','09:01','09:01']))