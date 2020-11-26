def solution(n,s):
    q, r = divmod(s, n)

    if q == 0:
        return [-1]
    
    result = [q] * n
    for i in range(len(result)-1,-1,-1):
        if r == 0:
            break
        else:
            r -= 1
            result[i] += 1
    
    return result