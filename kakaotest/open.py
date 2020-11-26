def change(answer, c_list,s_list,prior_name):
    i = 0
    while True:
        try:
            answer[c_list[i]] = s_list[2] + answer[c_list[i]][len(prior_name):]
        except:
            break
        i += 1
    return answer

def solution(record):
    answer = []
    
    mun = ["님이 들어왔습니다.","님이 나갔습니다."]
    
    user_dic = {}

    for s in record:
        s_list = s.split()
        #com, user_id, name
        if s_list[0] == 'Enter':
            answer.append(s_list[2]+mun[0])
            try:
                name, c_list = user_dic[s_list[1]]
                if name != s_list[2]:
                    prior_name = name
                    user_dic[s_list[1]][0] = s_list[2]
                    answer = change(answer, c_list, s_list, prior_name)
                user_dic[s_list[1]][1].append(len(answer) - 1)
            except:
                user_dic[s_list[1]] = [s_list[2],[(len(answer) - 1)]]
        elif s_list[0] == 'Leave':
            name = user_dic[s_list[1]][0]
            answer.append(name+mun[1])
            user_dic[s_list[1]][1].append(len(answer) - 1)

        else:
            prior_name = user_dic[s_list[1]][0]
            c_list = user_dic[s_list[1]][1]
            user_dic[s_list[1]][0] = s_list[2]
            answer = change(answer,c_list,s_list,prior_name)

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan","Change uid4567 abcde"]
print(solution(record))