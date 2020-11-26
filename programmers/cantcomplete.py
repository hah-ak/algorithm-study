def solution(participant,completion):
    dict_part = {}
    for p in participant:
        try:
            dict_part[p] += 1
        except:
            dict_part[p] = 1
    for c in completion:
        dict_part[c] -= 1
    
    for k,v in dict_part.items():
        if v > 0:
            return k

p = ['marina', 'josipa', 'vinko', 'vinko', 'filipa']
c = ['josipa', 'filipa', 'marina', 'vinko']

print(solution(p,c))