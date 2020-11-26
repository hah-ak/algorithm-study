def check_right(p):
    check = 0
    for i in range(len(p)):
        g = p[i]
        if g == '(':
            check += 1
        else:
            check -= 1
        if check < 0:
            return False
    return True
        

def solution(p):
    check = 0
    if p == "":
        return ""
    else:
        for i in range(len(p)):
            g = p[i]
            if g == '(':
                check += 1
            else:
                check -= 1
            if check == 0:
                u, v = p[:i+1], p[i+1:]
                if check_right(u):
                    return u + solution(v)
                else:
                    new_u = ""
                    for s in u[1:len(u)-1]:
                        if s == '(':
                            new_u += ")"
                        else:
                            new_u += "("
                    return "(" + solution(v) + ')' + solution(new_u)