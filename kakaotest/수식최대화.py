def calc(priority, n, expression):
    #('*', '-', '+'),0,# "100-200*300-500+20"
    if n == 2:
        return str(eval(expression))#'7+2' eval('7+2') => 9
        #('*', '-', '+'),0,# "100-200*300-500+20"
    if priority[n] == '*':
                            #('*', '-', '+'),0,# "100-200*300-500+20"
        res = eval('*'.join([calc(priority, n+1, e) for e in expression.split('*')]))
    if priority[n] == '+':
        res = eval('+'.join([calc(priority, n+1, e) for e in expression.split('+')]))
    if priority[n] == '-':
        res = eval('-'.join([calc(priority, n+1, e) for e in expression.split('-')]))
    return str(res)
    # "100-200*300-500+20"

def solution(expression):
    answer = 0
    priorities = [
        # 3순위 2순위 1순위
        ('*', '-', '+'),
        # ('*', '+', '-'),
        # ('+', '*', '-'),
        # ('+', '-', '*'),
        # ('-', '*', '+'),
        # ('-', '+', '*')
    ]
        #('*', '-', '+') 
    for priority in priorities:

                      #('*', '-', '+'),0,# "100-200*300-500+20"
        res = int(calc(priority, 0, expression))
        answer = max(answer, abs(res))
    
    return answer

print(solution('100-200*300-500+20'))