def split_str(string):
    string_dict = {}
    for i in range(2,len(string)+1):
        s = string[i-2:i]
        if s.isalpha(): 
            try:
                string_dict[s.upper()] += 1
            except:
                string_dict[s.upper()] = 1
    return string_dict

def solution(str1,str2):
    str1_dict, str2_dict = split_str(str1), split_str(str2) #2n
    
    inter_keys = list(set(str1_dict.keys() & str2_dict.keys())) # n
    only_str1_keys = list(set(str1_dict.keys() - inter_keys)) #n
    only_str2_keys = list(set(str2_dict.keys() - inter_keys)) #n
    
    union, inter = 0, 0
    for other in inter_keys: # 2n
        inter += min(str1_dict[other], str2_dict[other]) #1
        union += max(str1_dict[other], str2_dict[other]) #1
    for k in only_str1_keys: # n
        union += str1_dict[k]
    for k in only_str2_keys: # n
        union += str2_dict[k]
    if union == 0:
        return 65536
    return int(inter/union * 65536)

print(solution('FRANCE',"french"))