def dfs(o, i, idx,menu,step):
    global candi_dic, check_list
    if step == i:
        menu = list(menu)
        menu.sort()
        menu = "".join(menu)
        try:
            candi_dic[i][menu] += 1
        except:
            candi_dic[i][menu] = 1
    elif step > i:
        None
    else:
        for j in range(idx,len(o)):
            if check_list[j] == False:
                check_list[j] = True
                menu += o[j]
                dfs(o, i, j ,menu, step + 1)
                menu = menu[:-1]
                check_list[j] = False
def solution(orders, course):
    global candi_dic, check_list
    candi_dic = {}
    for c in course:
        candi_dic[c] = {}
        
    for i in course:
        for o in orders:
            if len(o) >= i:
                check_list = [False] * len(o)
                dfs(o, i,0,"" ,0)
    result = []
    for c in course:
        try:
            m = max(candi_dic[c].values())
            if m >= 2:
                for k, v in candi_dic[c].items():
                    if v == m:
                        result.append(k)
        except:
            None
    result.sort()
    return result
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))