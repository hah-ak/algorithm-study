def solution(number, k):
    start = 1
    while k != 0:
        check = True
        for i in range(start,len(number)):
            if number[i-1] < number[i]:
                number = number[:i-1] + number[i:]
                k -= 1
                if i-1 <= 0:
                    start = 1
                else:
                    start = i - 1
                check = False
                break
        if check == True:
            number = number[:len(number)-k]
            break
    return number




# 승진이형 풀이
def solution(number, k):
    max_idx = 0
    result = []
    # 과정을 반복한다.
    # 커서의 위치 인덱스
    idx = 0
    while True :
        # number[idx:idx+k] 중에서 최대값 인덱스 찾기
        # 부분 최대값의 인덱스는 max_idx
        max_idx = number[idx:idx+k+1].find(max(number[idx:idx+k+1]))
        a = number[idx:idx+k+1]
        # idx += (max_idx + 1)
        idx += (max_idx + 1)
        # 최대값만 result에 담는다.
        result += number[idx-1]
        # k -= max_idx
        k -= max_idx
        # k == 0 이면 result += number[idx:]
        if k <= 0:
            result += number[idx:]
            break
    return ''.join(result)

print(solution("99999321",2))