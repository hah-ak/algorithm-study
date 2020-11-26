def solution(files):
    h_n_t_list = []
    for file in files:
        h_n_t = ["","",file]
        check = False
        for s in file:
            if not s.isnumeric():
                if check == True:
                    break
                h_n_t[0] += s.lower()
            else:
                check = True
                h_n_t[1] += s
        h_n_t[1] = int(h_n_t[1])
        h_n_t_list.append(h_n_t)
    h_n_t_list.sort(key = lambda x : (x[0],x[1]))
    return [file_name for _,_,file_name in h_n_t_list]

files = ['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']
print(solution(files))
s='ab3'

