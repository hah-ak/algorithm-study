def dfs(water,me,step):
    new_water = []
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while water:
        x,y = water.pop()
        for i in range(4):
            if (0 <= x - dx < len(location)) and (0 <= y - dy < len(location)):
                if location[x-dx][y-dy] == 0:
                    location[x-dx][y-dy] = 'w'
                    new_water.append([x-dx,y-dy])
    x, y = me
    for i in range(4):
        if (0 <= x - dx < len(location)) and (0 <= y - dy < len(location)):
            if location[x-dx][y-dy] == 'w':
                return step
            elif location[x-dx][y-dy] == 0:
                location[x-dx][y-dy] = 'm'
                
                
    
N = int(input())
location = []
for _ in range(N):
    location.append(list(map(int,input().split())))

water = [0,0]
me = [N-1,N-1]
