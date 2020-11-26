def solution(n,build_frame):
    board = []
    for i in range(n+1):
        add = []
        for j in range(n+1):
            add.append([])
        board.append(add)

    #result x y a
    result = []
    location_dic = {}
    # x, y a(0기둥, 1보) b(0삭 1설)
    for i in range(len(build_frame)):
        x, y, a, b = build_frame[i]
        if a == 0:
            if b == 1:
                if y == 0 or 0 in board[x][y] or 1 in board[x][y]:
                    board[x][y+1].append(0)
                    board[x][y].append(0)
                    location_dic[f'{x}{y}{a}'] = 0
            else:
                n = board[x][y+1].count(0)
                if n == 1:
                    board[x][y+1].remove(0)
                    board[x][y].remove(0)
                    location_dic.pop(f'{x}{y}{a}')
        else:
            n = board[x][y].count(0)
            m = board[x+1][y].count(0)
            o = board[x][y].count(1)
            p = board[x+1][y].count(1)
            if b == 1:
                
                if n == 1 and m <= 1:
                    board[x][y].append(1)
                    board[x+1][y].append(1)
                    location_dic[f'{x}{y}{a}'] = 0
                elif m == 1 and n <= 1:
                    board[x][y].append(1)
                    board[x+1][y].append(1)
                    location_dic[f'{x}{y}{a}'] = 0
                elif n == 0 and m == 0 and o > 0 and p > 0:
                    board[x][y].append(1)
                    board[x+1][y].append(1)
                    location_dic[f'{x}{y}{a}'] = 0
            else:
                if o > 1 and p > 1:
                    board[x][y].remove(1)
                    board[x+1][y].remove(1)
                    location_dic.pop(f'{x}{y}{a}')
                elif n == 0 and p > 1:
    for k in location_dic.keys():
        result.append(list(map(int,k.split(','))))
    result.sort(key = lambda x: (x[0],x[1],x[2]))
    print(result)
    return result

print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))