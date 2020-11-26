def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        mid_answer = len(s)
        add_num = [1]
        end = i
        now_char = s[0:end]
        while end+i <= len(s):
            if now_char == s[end:end+i]:
                mid_answer -= i
                add_num[-1] += 1
                end += i
            else:
                end += i
                now_char = s[end-i:end]
                add_num.append(1)
        add = 0
        for a in add_num:
            if a != 1:
                add += len(str(a))
        if answer > mid_answer + add:
            answer = mid_answer + add
    return answer

print(solution("xababcdcdababcdcd"))