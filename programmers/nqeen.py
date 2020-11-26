def dfs(row, unuse):
    global N, answer,check_column
    if row == N:
        answer += 1
    else:
        for i in range(N):
            if (check_column[i] == False) and (i not in unuse):
                check_column[i] = True
                unu = []
                if 0 <= i - 1:
                    unu.append(i-1)
                if i + 1 < N:
                    unu.append(i+1)
                dfs(row + 1, unu)
                check_column[i] = False


def solution(n):
    global N, answer, check_column
    N, answer = n, 0
    check_column= [False] * n
    dfs(0,[])
    return answer