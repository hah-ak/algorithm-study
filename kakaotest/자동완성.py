import sys
sys.setrecursionlimit(10**6)
def check(fin_word,word, dic_word):
    if word == "":
        return len(fin_word)
    if dic_word[word[0]]['step_child'][1] == 1:
        return dic_word[word[0]]['step_child'][0]
    return check(fin_word,word[1:], dic_word[word[0]])

def tri(dic_word,word,step):
    if word != "":
        try:
            dic_word[word[0]]['step_child'][1] += 1
            tri(dic_word[word[0]],word[1:],step + 1)
        except:
            dic_word[word[0]] ={}
            dic_word[word[0]]['step_child'] = [step,1]
            tri(dic_word[word[0]],word[1:],step + 1)


def solution(words):
    answer = 0
    dic_word = {}
    for word in words:
        tri(dic_word,word,1)
    print(dic_word)
    for word in words:
        answer += check(word,word, dic_word)
    return answer


print(solution(['word','war','warrior','world']))