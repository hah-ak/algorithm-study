def div(n_10, n):
    s = '0123456789ABCDEF'
    q,r = divmod(n_10,n)
    if q == 0:
        return s[r]
    return div(q, n) + s[r]
def solution(n,t,m,p):
    answer = ""
    
    now_n = ""
    n_10 = 0
    while True:
        now = div(n_10, n)
        now_n += now
        if len(now_n) >= t*m:
            break
        n_10 += 1
    
    for i in range(0,t):
        answer += now_n[i*m + p-1]
    return answer

print(solution(16,16,2,2))