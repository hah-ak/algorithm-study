def solution(gems):
    len_and_result = [len(gems),0,len(gems)-1]
    set_gems = list(set(gems))
    gem_names = {}
    for name in set_gems:
        gem_names[name] = 0
    start = 0
    for i in range(len(gems)): #실제로 4번째 에서 끝남
        gem_names[gems[i]] += 1
        if 0 not in gem_names.values():
            len_and_result[2] = i
            gem_names[gems[i]] -= 1 # 그래서 빼줌.
            break
    
    for i in range(len_and_result[2],len(gems)):# 여기서도 4번째 시작시 중복이 생김,
        gem_names[gems[i]] += 1
        #if 0 not in gem_names.values(): 최초위치
        while True:
            if gem_names[gems[start]] - 1 < 1:
                if i - start < len_and_result[0]:
                    len_and_result = i - start, start, i
                break
            else:
                gem_names[gems[start]] -= 1
                start += 1
    
    return [len_and_result[1]+1, len_and_result[2]+1]
            


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))


    
