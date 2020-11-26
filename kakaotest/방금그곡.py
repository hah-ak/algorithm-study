def seperate(melody):
    melody_list = []
    for j in range(len(melody)):
        if melody[j] == "#":
            melody_list[-1] += "#"
        else:
            melody_list.append(melody[j])
    return melody_list

def solution(m,musicinfos):
    m_list = seperate(m)
    candidate = [0,""]
    for music in musicinfos:
        S, E, song, melody = music.split(',')
        time_list = [S,E]
        for i in range(2):
            hour, minu = map(int, time_list[i].split(":"))
            hour = hour * 60
            time_list[i] = hour + minu
        time = time_list[1] - time_list[0]
        
        melody_list = seperate(melody)
        
        q, r = divmod(time, len(melody_list))
        all_melody_list = melody_list * q + melody_list[:r]

        
        for k in range(len(all_melody_list)+1-len(m_list)):
            if all_melody_list[k:k+len(m_list)] == m_list:
                if time > candidate[0]:
                    candidate[1] = song
    if candidate[1] != "":
        return candidate[1]
    return '(None)'

print(solution('C#DE',['12:00,12:3,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF']))