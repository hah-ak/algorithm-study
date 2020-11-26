def solution(word,pages):
    # 키는 현재 웹 도메인,인덱스, 기본점수, 외부링크 수, 링크 점수, 매칭점수, 외부링크 리스트,외부링크 점수합
    #                       0       1       2           3           4           5           6
    site_dic = {}
    # 링크 점수는 현재웹에 연결된 링크의 기본점수 // 외부링크 수
    # 매칭점수는 기본점수 + 링크점수
    
    ind = 0
    for page in pages:
        page_list = page.split('\n')
        now_web = page_list[3].split()
        now_web = now_web[-1][9:-3]
        site_dic[now_web] = [ind,0,0,0,0,[],0]
        check_body = False
        for line in page_list:
            if line == "":
                continue
            if line == '<body>':
                check_body = True
                continue
            if line == '</body>':
                break
            if check_body:
                line = line.replace('<a',' ').replace('</a>',' ')
                line_list = line.split()
                for string in line_list:
                    if string[:4] == 'href':
                        strings = string.split('">')
                        site_dic[now_web][2] += 1
                        site_dic[now_web][5].append(strings[0][6:])
                        for strs in strings[1:]:
                            start = 0
                            for i in range(1, len(strs)+1):
                                if not strs[i-1:i].isalpha():
                                    
                                    if word.lower() == strs[start:i-1].lower():
                                        site_dic[now_web][1] += 1
                                    start = i
                            if word.lower() == strs[start:len(strs)].lower():
                                # print(strs[start:len(strs)])
                                site_dic[now_web][1] += 1
                    else:
                        start = 0
                        for i in range(1, len(string)+1):
                            if not string[i-1:i].isalpha():
                                
                                if word.lower() == string[start:i-1].lower():
                                    site_dic[now_web][1] += 1
                                start = i
                        if word.lower() == string[start:len(string)].lower():
                            print(string[start:len(string)])
                            site_dic[now_web][1] += 1
                    
                # if line[:9] == '<a href="':
                #     strings = line.split('">')
                #     site_dic[now_web][2] += 1
                #     site_dic[now_web][5].append(strings[0][9:])
        ind += 1
    
    # for k, v in site_dic.items():
    #     print(k, v)

    for k, v in site_dic.items():
        for web in v[5]:
            try:
                site_dic[web][6] += v[1]
            except:
                None
    matching_list = [0] * len(site_dic.keys())
    for k, v in site_dic.items():
        try:
            matching_list[v[0]] = v[1] + v[6] // v[2]
        except:
            None
    return matching_list.index(max(matching_list))

pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&muzi\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution('muzi',pages))
s= "123"
s = s.replace('1','2')
print(s)