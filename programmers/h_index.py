def solution(citations):
    
    answer = 0
    citations.sort()
    
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            answer = len(citations) - i
            break
    return answer
citations = [3,0,6,1,6]
print(solution(citations))