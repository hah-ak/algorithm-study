def solution(n,delivery):
    delivery.sort(key = lambda x:x[2], reverse= True)
    check = ['?'] * (n+1)

    for f, s , c in delivery:
        if c == 0:
            check[f] = 'o'
            check[s] = 'o'
        else:
            if f == 'o':
                check[s] = 'x'
            elif s == 'o':
                check[f] = 'x'

    
    return ''.join(check)[1:]