import sys
sys.setrecursionlimit


def dfs(myMap, n, m, row, column):
    
    if 1 not in myMap:
        return 0
    elif row == n and column == m-1:
        return 0
    temp = []
    dxy = [[0,0],[0,-1],[0,1],[1,0],[-1,0]]
    for i in range(row, n):
        for j in range(column, m):
            if myMap[i][j] == 1:

                white, black = [], []
                for dx, dy in dxy:
                    
                    if 0 <= i + dy < n and 0 <= j + dx < m:
                        if myMap[i+dy][j+dx] == 1:
                            black.append([i+dy, j+dx])
                        else:
                            white.append([i+dy, j+dx])

                if len(black) > len(white):
                    for y, x in black:
                        myMap[y][x] = 0
                    for y, x in white:
                        myMap[y][x] = 1
                    temp.append(dfs(myMap, n, m, i, j))
                    
                    for y, x in black:
                        myMap[y][x] = 1
                    for y, x in white:
                        myMap[y][x] = 0
    if temp:                    
        result = 1+ min(temp)
        return result
    else:
        return 1

def flip(myMap, n, m):
    
    answer = dfs(myMap, n, m, 0, 0)



    return answer