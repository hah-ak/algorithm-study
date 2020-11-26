def bfs(v,s,now):
    if s == []:
        return v
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    len_row = len(v)
    len_c = len(v[0])
    r,c = s.pop(-1)
    v[r][c] = -1
    for i in range(4):
        if -1 < r + dx[i] < len_row and -1 < c + dy[i] < len_c:
            if now == v[r + dx[i]][c + dy[i]]:
                v[r + dx[i]][c + dy[i]] = -1
                s.append([r + dx[i],c + dy[i]])
    return bfs(v,s,now)

def solution(v):
    answer = [0,0,0]
    for r in range(len(v)):
        for c in range(len(v[0])):
            if v[r][c] != -1:
                now = v[r][c]
                v = bfs(v,[[r,c]],now)
                answer[now] += 1
    
    return answer

print(solution([[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]]))