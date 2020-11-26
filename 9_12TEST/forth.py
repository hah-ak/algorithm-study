def dfs(start,goal,start_end_list,fee,check_list):
    


def make_money(start,start_end_list,goal):
    money = 100000*200*200
    check = False
    if start == goal:
        return 0
    check_list = []
    check_list.append(start)
    fee = 0
    s = start
    while True:
        if s == goal:
            if money > fee:
                money = fee
                break
        else:
            check = False
            for e,f in start_end_list[s]:
                if e not in check_list:
                    check_list.append(e)
                    fee += f
                    s = e
                    check = True
                    break
            if check== False:
                a = check_list.pop(-1)
                no_use.append(a)
    return money

def solution(n,s,a,b,fares):
    add_fares = []
    for q,w,e in fares:
        add_fares.append([w,q,e])
    fares += add_fares

    start_end_list = []
    for _ in range(n):
        start_end_list.append([])

    for q,w,e in fares:
        start_end_list[q-1].append([w-1,e])
    for i in range(len(start_end_list)):
        start_end_list[i].sort(key = lambda x: x[1])

    result = 100000*200*200
    for i in range(n):
        start = i
        sums = 0
        for goal in [s,a,b]:
            sums += make_money(start,start_end_list,goal-1)
        if sums < result:
            result = sums
    return result

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))