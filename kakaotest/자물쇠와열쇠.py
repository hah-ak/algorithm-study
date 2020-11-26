def solution(key, lock):
    lock_location = []
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                lock_location.append([i,j])
    if lock_location == [] and 1 not in key:
        return True
    c = 0
    while c < 4:    
        key_location = []
        for i in range(len(key)):
            for j in range(len(key)):
                if key[i][j] == 1:
                    key_location.append([i,j])
        for k in key_location:
            diff = [lock_location[0][0]-k[0], lock_location[0][1]-k[1]]
            new_k = []
            dontfor = False
            for l in key_location:
                if 0 <= l[0] + diff[0] < len(lock) and 0 <= l[1] + diff[1] < len(lock): 
                    if lock[l[0] + diff[0]][l[1] + diff[1]] != 1:
                        new_k.append([l[0] + diff[0], l[1] + diff[1]])
                    else:
                        dontfor = True
                        break
                else:
                    pass

            if not dontfor:
                check = True
                for m in lock_location:
                    if m not in new_k:
                        check = False
                if check == True:
                    return True

        trans_key = []
        for i in range(len(key)):
            add = []
            for j in range(len(key)):
                add.append(key[j][i])
            trans_key.append(add[::-1])
        key = trans_key
        c += 1
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))