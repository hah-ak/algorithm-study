def solution(clothes):
    answer = 0
    clothe_dic = {}
    for c, s in clothes:
        try:
            clothe_dic[s] += 1
        except:
            clothe_dic[s] = 1
    
    V = list(clothe_dic.values())
    for i in range(len(V)):
        j = 1
        for v in range(i << len(V)-i):
            j *= V[v]
        answer += j
    print(answer)
    return answer

solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear'],[4,3]])