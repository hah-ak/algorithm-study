def dfs(cnt,now_c,length,true_list,relation,ind):
    global add_list, check_list
    # 갯수만큼 컬럼이 잡혔다면, 호부키가 될 요건이 되는지 알아본다
    if cnt == now_c:
        if true_list:
            key_dic = {}
            for r in relation: # 선택된 칼럼들중에 중복되는게 잇는지 없는지 알아본다.
                check_key = ','.join([r[j] for j in true_list])
                try:
                    key_dic[check_key] += 1
                    return
                except:
                    key_dic[check_key] = 0
            add_list.append(true_list)
    else:
        # cnt갯수 만큼 컬럼을 골라내는 작업
        for i in range(ind,length): # 이미 1번 인댁스를 선택했다면, 그 이전 값을 볼 필요가 없으므로 ind값 부터 시작한다
            if check_list[i] == False:
                check_list[i] = True
                dfs(cnt,now_c+1,length,true_list+[i],relation,i+1)
                check_list[i] = False

# 

def solution(relation):
    global add_list, check_list
    result_list = []
    check_list = [False] * len(relation[0]) # 반복문을 돌때, 중복된 칼럼 선택을 방지하게 하기위해 만드어준다.
    cnt = 1 # 선택할 칼럼의 갯수
    # 반복문을 통해 1개를 선택할때부터 전부 선택할때 까지 돌게 된다.
    while cnt < len(relation)+1:
        add_list = [] # 추가될 가능성이 있는 리스트를 만들어낸다
        dfs(cnt,0,len(relation[0]),[],relation,0)
        mid_list = [] 
        # 추가된 리스트 중에서 result값과 중복되는게 있는지 찾는다.
        for add in add_list:
            check_add = True
            for r in result_list:    
                if set(r) == set(set(add) & set(r)): # 만약 add_list의 어떤 원소가 result_list의 어떤 원소와 중복이 된다면 더이상 그 원소에 대해서 검사할 필요가 없다.
                    check_add = False
                    break
            if check_add:
                mid_list.append(add)
        #     for i in add:
        #         check_list[i] = True
        result_list += mid_list
        cnt += 1

    return len(result_list)
    