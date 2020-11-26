def solution(phone_book):
    use_list = phone_book
    use_list.sort(key = lambda x: len(x))
    while use_list:
        for i in range(1,len(use_list)):
            if use_list[0] == use_list[i][:len(use_list[0])]:
                return False
        use_list = use_list[1:]
    return True

print(solution(['12','123','1235','567','88']))