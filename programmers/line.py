def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


def solution(n,k):
    n_list = [i for i in range(1,n+1)]
    now_part = factorial(n)
    
    # 사전순으로 나열되므로 구간별로 특정한 패턴이 있을것임
    # k번이 나올때까지 제일 앞 숫자부터 구간으로 나누어서
    # 찾아가는 형태로만든다
    answer = []
    while n_list:
        now_part = now_part // n
        # 각 구간은 나머지가 0이 되는 부분까지이고, 0일때까지 몫이 같으므로
        # 한칸씩 밀리게된다
        q, r = divmod(k, now_part)
        # q는 현재 칼럼(구간)의 인덱스가 된다.
        if r == 0:
            q -= 1
        answer.append(n_list.pop(q))
        k, n = r, n-1

    
    return answer


print(solution(5,2))
# print(1//5)