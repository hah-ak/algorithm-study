def solution(works,n):
    if len(works) == 1:
        return (works[-1] - n) **2 if works[-1] - n > 0 else 0
    works.sort(reverse = True)
    ind = 1
    while n > 0 and ind != len(works):
        if works[ind-1] != works[ind]:
            x = n - ((works[ind-1] - works[ind]) * ind)
            if x > 0:
                for i in range(ind):
                    works[i] -= x
                    n -= x
            else:
                for i in range(ind):
                    if n != 0:
                        works[i] -= 1
                        n -= 1
        ind += 1
    if n > 0:
        if works[0] * len(works) - n < 0:
            return 0
        else:
            
    else:
        return sum([i ** 2 for i in works])
     

print(solution([4,1,2],3))