import sys
sys.setrecursionlimit(10 ** 6)

def checking(word,queries_dic):
    try:
        r = queries_dic['idx']
    except:
        r = []
    try:
        q = queries_dic[word[0]]
        return r + checking(word[1:], q)
    except:
        return r
        


def tri(queries_dic,query,idx):
    if query[0] == '?':
        try:
            queries_dic['idx'].append(idx)
        except:
            queries_dic['idx'] = [idx]
    else:
        if query[0] not in queries_dic.keys():
            queries_dic[query[0]] = {}
        queries_dic[query[0]].update(tri(queries_dic[query[0]], query[1:], idx))
    return queries_dic
    
def solution(words,queries):
    result= [0] * len(queries)
    queries_dic = {}
    queries_dic['normal'] ={}
    queries_dic['reverse'] = {}
    idx = 0
    for query in queries:
        if query[0] == '?':
            try:
                queries_dic['reverse'][len(query)] = tri(queries_dic['reverse'][len(query)],query[::-1],idx)
            except:
                queries_dic['reverse'][len(query)] = {}
                queries_dic['reverse'][len(query)] = tri(queries_dic['reverse'][len(query)],query[::-1],idx)
                    
            
        else:
            try:
                queries_dic['normal'][len(query)] = tri(queries_dic['normal'][len(query)],query,idx)
            except:
                queries_dic['normal'][len(query)] = {}    
                queries_dic['normal'][len(query)] = tri(queries_dic['normal'][len(query)],query,idx)
        idx += 1
    
    for word in words:
        r_word = word[::-1]
        idx_list = []
        try:
            q = queries_dic['normal'][len(word)]
            idx_list += checking(word,q)
        except:
            pass
        try:
            q = queries_dic['reverse'][len(word)]
            idx_list += checking(r_word, q)
        except:
            pass
        for idx in idx_list:
            result[idx] += 1
    # print(queries_dic.items())    
    return result

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "fr???", "fro???", "pro?",'frod?','?????','?rodo']
# queries = ['?????']
print(solution(words,queries))

