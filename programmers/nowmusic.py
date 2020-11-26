def um_trans(um):
    um_list = []
    for u in um:
        if u == "#":
            um_list[-1] += "#"
        else:
            um_list.append(u)

    return um_list

def solution(m, musicinfos):
    m_list = um_trans(m)
    for music in musicinfos:
        s,e,title,um = music.split(',')
        s_h,s_m = map(int, s.split(':'))
        e_h,e_m = map(int, e.split(':'))
        time = (e_h-s_h)*60 + (e_m - s_m)
        
        um_list = um_trans(um)
        all_um = []
        
        for i in range(time):
            all_um.append(um_list[i % len(um_list)])
        
        for i in range(len(all_um)-len(m_list)):
            if all_um[i:i+len(m_list)] == m_list:
                return title
    return None

print(solution("CC#BCC#BCC#BCC#B",['03:00,03:30,FOO,CC#B','04:00,04:08,BAR,CC#BCC#BCC#B']))