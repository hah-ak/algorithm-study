def solution(encrypted_text, key, rotation):
    answer = ''
    

    _ , rotation = divmod(rotation, len(key))
    encrypted_text = encrypted_text[rotation:] + encrypted_text[:rotation] 
    
    dic = {}
    abc = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(abc)):
        dic[abc[i]] = i
    
    for i in range(len(encrypted_text)):
        num = dic[encrypted_text[i]] - dic[key[i]] - 1
        if num < 0:
            answer += abc[num + len(abc)]
        else:
            answer += abc[num]
    return answer

print(solution('sssss','',-9))