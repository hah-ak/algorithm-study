import sys
sys.setrecursionlimit(10**10)

# def deletes(s):
#     i = 0
#     d_list = []
#     set_s = set(range(len(s)))
#     while i < len(s)-1:
#         i += 1
#         if s[i] == s[i-1]:
#             d_list += [i,i-1]
#             i += 2
        
#     new_set = set(set_s - set(d_list))
#     new_s = ""
#     for j in list(new_set):
#         new_s += s[j]
#     return new_s

def solution(s):
    if s != "":
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                return solution(s[:i-1]+s[i+1:])
        return 0
    else:
        return 1

    # while s != "":
    #     check = len(s)
    #     s= deletes(s)
    #     if check == len(s):
    #         return 0
    # return 1

s = 'baabaa'       
print(solution(s))