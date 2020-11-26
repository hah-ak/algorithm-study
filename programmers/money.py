def solution(n,money):
    
    money.sort()
    money_to_money = [1] * len(money)
    for i in range(1,len(money)):
        cnt, j = 0, 1
        use_money = [0] * (i)
        m = money[i]
        while j <= i:
            if m == 0:
                use_money[i-j] = cnt 
                j += 1
                cnt = 0
            if m - money[i-j] >= 0:
                m -= money[i-j]
                cnt += 1
            else: 
                j += 1
                cnt = 0
        add = 0
        for k in range(1,i):
            add += (money[k] * use_money[k])
        money_to_money[i] += add
    
    idx = -1
    min_exchange = [0] * len(money)
    while n > 0:
        if n - money[idx] >= 0:
            n -= money[idx]
            min_exchange[idx] += 1
        else:
            idx -= 1
    result = 1
    for l in range(len(money)):
        if min_exchange[l] != 0:
            result *= (min_exchange[l] * money_to_money[l])

    return result % 1000000007


print(solution(5,[1,2,5]))

