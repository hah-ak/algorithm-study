def solution(n,lost,reserve):
    
    overlap = list(set(lost) & set(reserve))
    lost = list(set(lost) - set(overlap))
    reserve = list(set(reserve) - set(overlap))
    for r in reserve:
        if (r-1) in lost:
            lost.remove(r-1)
        elif (r+1) in lost:
            lost.remove(r+1)
    
    return n-len(lost)

print(solution(10,[1,2,6,8,10],[3,7,9]))