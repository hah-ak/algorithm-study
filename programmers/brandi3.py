import sys
sys.setrecursionlimit(10**6)

def solution(step, start,result):
    global MIN, N, M, answer
    if step > M:
        None
    elif start == N:
        if result < MIN:
            MIN = result
    else:
        for k in node_dic[start].keys():
            if node_dic[start][k][1] == 0:
                node_dic[start][k][1] = result + node_dic[start][k][0]
                solution(step + 1, k, node_dic[start][k][1])
                node_dic[start][k][1] = 0
            else:
                if node_dic[start][k][1] > node_dic[start][k][0] + result:
                    answer = 'bug'
                else:
                    None

MIN = 10000000
answer = ''
N, M = map(int, input().split())
node_dic = {}
for _ in range(M):
    s , e , sec = list(map(int, input().split()))
    try:
        node_dic[s][e]= [sec, 0]
    except:
        node_dic[s] = {
            e: [sec, 0]
        }

solution(0,1,0)
if MIN == 10000000 or answer == 'bug':
    print('bug')
else:
    print(MIN)