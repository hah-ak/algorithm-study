def solution(people,limit):
    answer = 0
    people.sort(reverse = True)
    SUM = 0
    s,e = 0, len(people) - 1
    while s <= e:
        if SUM + people[e] > limit:
            answer += 1
            SUM = 0
        else:
            if SUM + people[s] <= limit:
                SUM += people[s]
                s += 1
            else:
                SUM += people[e]
                e -=1
        
    return answer + 1 #가장 마지막 리스트는 어떠한 경우에도 더 해지지 않으므로 +1 해준다.