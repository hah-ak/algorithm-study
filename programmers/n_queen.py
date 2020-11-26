import sys
sys.setrecursionlimit(100000)

def check_parel(row, i, checkList):
    
    for j in range(len(checkList)):
        if checkList[j] != 'useable':
            x, y = checkList[j] - row, j - i
            try:
                a = y / x
                if a == 1 or a == -1:
                    return False
            except:
                None
    return True
    
def dfs(n, row, checkList):
    
    if row == n:
        if 'useable' not in checkList:
            return 1
        else:
            return 0
    result = 0
    for i in range(n):
        if checkList[i] == 'useable':
            check = check_parel(row, i, checkList)
            if check:
                checkList[i] = row
                result += dfs(n, row + 1, checkList)
                checkList[i] = 'useable'
    return result
def nQueen(n) :
    '''
    n개의 Queen을 배치하는 경우의 수를 반환하는 함수를 작성하세요.
    '''
    checkList = ['useable'] * n # column 별 퀸의 row를 담는다
    answer = dfs(n, 0, checkList)
    return answer

print(nQueen(4))
