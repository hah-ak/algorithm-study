def binary(n,weak, dist):
    
    return

def solution(n, weak, dist):

    result = 0
    
    dist.sort()
    start, end = 0, -1
    while weak:
        min_w, max_w = weak[start], weak[end]
        if max_w - min_w <= dist[-1]:
            weak = weak[:start] + weak[end:]
            start, end = 0, -1
            result += 1
        elif min_w + n - max_w <= dist[-1]:
            weak = weak[start:end]
            start, end = 0, -1
            result += 1
        else:
            
    return