def tri(m, char_dic,max_idx):
    idx = 0
    if len(m) == 0:
        return m, char_dic['_index'], max_idx
    try:
        char_dic[m[0]]
        m, idx, max_idx = tri(m[1:], char_dic[m[0]],max_idx)
    
    except:
        idx = char_dic['_index']
        char_dic[m[0]] = {}
        max_idx += 1
        char_dic[m[0]]['_index'] = max_idx
    return m, idx, max_idx

def solution(msg):
    answer = []
    idx = 1
    char_dic = {}
    for i in range(ord('A'),ord('Z')+1):
        char_dic[chr(i)] = {}
        char_dic[chr(i)]['_index'] = idx
        idx += 1
    max_idx = 26
    start = 0
    while msg:
        msg, idx, max_idx = tri(msg,char_dic,max_idx)
        answer.append(idx)
    return answer

print(solution('KAKAO'))