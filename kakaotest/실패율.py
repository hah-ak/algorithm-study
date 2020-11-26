def solution(N,stages):
    now = [0] * (N+2)
    
    for stage in stages:
        now[stage] += 1

    all_member = now.copy()
    for i in range(len(all_member) -2,-1,-1):
        all_member[i] = all_member[i + 1] + all_member[i]

    for i in range(1,N+1):
        try:
            now[i] = now[i] / all_member[i]
        except:
            now[i] = 0
    answer = list(enumerate(now))[1:N+1]
    answer.sort(key = lambda x:x[1],reverse = True)
    return [i for i, _ in answer]
print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))