# 움직이는 패턴이 존재한다.
# 여기서 링이 움직이는건 봉이 움직이는 것과 같이 볼 수 있다.
def hanoi(n,from_pos, to_pos, aux_pos):
    global lis
    if n == 1:
        lis.append([from_pos,to_pos])
        return
    hanoi(n-1, from_pos, aux_pos,to_pos)
    lis.append([from_pos,to_pos])
    hanoi(n-1,aux_pos, to_pos, from_pos)

def solution(n):
    global lis
    lis = []
    hanoi(n,1,3,2)
    return lis

print(solution(3))