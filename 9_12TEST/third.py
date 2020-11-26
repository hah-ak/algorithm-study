# def make_dic(dic_info, qu,step):
#     # r = [[dic_info,qu]]
#     # result = []
#     # while r:
#     #     check, now_qu = r.pop(-1)
#     #     if type(now_qu[0]) == int:
#     #         for k, v in check.items():
#     #             if k <= qu[-1]:
#     #                 result += v
#     #     else:
#     #         for k, v in check.items():
#     #             if now_qu[0] == k or k == '-':
#     #                 r.append([check[k],now_qu[1:]])

#     # return result
#     if len(qu)-1 == step:
#         r = []
#         for k, v in dic_info.items():
#             if k <= qu[-1]:
#                 r += v
#         return r
#     else:
#         r = []
#         for k,_ in dic_info.items():
#             if qu[step] == k or k == '-':
#                 r += make_dic(dic_info[k],qu,step+1)
    # return r
def make(dic_query,idx,query):
    if len(query) == 1:
        if query[-1] in dic_query.keys():
            dic_query[query[-1]].append(idx)
        else:
            dic_query[query[-1]] = [idx]
        return dic_query
    if query[0] == "-":
        for k, v in dic_query.items():
            dic_query[k] = make(dic_query[k],idx,query[1:])
    else:
        dic_query[query[0]] = make(dic_query[query[0]],idx,query[1:])
    return dic_query

def solution(info, query):
    dic_query = {}
    lang = ['cpp','java','python']
    jik = ['backend','frontend']
    gyung = ['junior','senior']
    food = ['chicken','pizza']
    for l in lang:
        if l not in dic_query.keys():
            dic_query[l] = {}
        for j in jik:
            if j not in dic_query[l].keys():
                dic_query[l][j] = {}
            for g in gyung:
                if g not in dic_query[l][j].keys():
                    dic_query[l][j][g] = {}
                for f in food:
                    if f not in dic_query[l][j][g].keys():
                        dic_query[l][j][g][f] = {}
    idx = 0
    for que in query:
        qu = que.split()
        qu_list = []
        for q in qu:
            if q != 'and':
                qu_list.append(q)
        qu_list[-1] = int(qu_list[-1])
        #언어 직군 경력 푸드 점수
        # dic_query = make(dic_query,idx,qu_list)
        
        dic_query = make(dic_query,idx,qu_list)
        idx += 1
    result =[0] * len(query)
    
    for infor in info:
        infor = infor.split()
        infor[-1] = int(infor[-1])
        a,b,c,d,e = infor
        for k, v in dic_query[a][b][c][d].items():
            if k <= e:
                for i in dic_query[a][b][c][d][k]:
                    result[i] += 1
    return result
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150","java and backend and junior and pizza 110","java and backend and junior and chicken 100","java and backend and junior and - 70", "cpp and - and senior and pizza 150"]

print(solution(info, query))