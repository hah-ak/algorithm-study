def combination(n, k):
    
    N, K = 1, 1
    while k > 0:
        
        N *= n
        K *= k
        n, k = n - 1, k - 1
        
    return N // K



def solution(n):
    answer = 0
    k = 0
    while n > 0:
        
        answer += combination(n, k)
        k += 1
        n -= 1

    return answer % 1234567

print(solution(4))