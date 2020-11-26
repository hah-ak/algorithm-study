def dfs(numbers,target,row,result):
    global answer
    if row > len(numbers):
        None
    elif (row == len(numbers)) and (target == result):
        answer += 1
    elif (row == len(numbers)) and (target != result):
        None
    else:
        for i in [1,-1]:
            dfs(numbers,target,row+1,result + numbers[row] * i)

def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers,target,0,0)
    return answer

print(solution([1,1,1,1,1],3))