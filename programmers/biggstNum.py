def solution(numbers):
    
    numbers = list(map(str, numbers))
    
    numbers.sort(key = lambda x: x*3, reverse = True)
    
    if numbers[0] == 0:
        return '0'
    return ''.join(numbers)

print(solution([0,0,0,0,10,101,1000,111]))
