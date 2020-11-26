def solution(expression):
    
    num_list = []
    ope_list = []
    num = ""
    for e in expression:
        if e.isnumeric():
            num += e
        else:
            num_list.append(int(num))
            ope_list.append(e)
            num = ""
    
    
    
    return
