def solution(s):
    if len(s) == 1:
        return 1
    elif len(s) == 2:
        if s[0] == s[1]:
            return 2
        return 1
    answer = 0
    for i in range(1,len(s)-1):
        length_1, length_2 = 0, 0
        check_1, check_2 = True, True
        for j in range(i+1):

            if check_1 and -1 < i - j and i + j < len(s):
                if s[i-j] != s[i+j]:
                    check_1 = False
                else:
                    length_1 = j*2 +1

            if check_2 and -1 < i - j and i + j + 1 < len(s):
                
                if s[i-j] != s[i+j+1]:
                    check_2 = False
                else:
                    length_2 = j*2 + 2
                    
            if (not check_1) and (not check_2):
                break
        
        length = max(length_1, length_2)
        if length > answer:
            answer = length
        
    
    return answer