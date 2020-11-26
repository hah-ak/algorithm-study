def solution(m,n,board):
    answer = 0
    
    trans_board = []
    for i in range(n):
        trans_list = []
        for j in range(m):
            trans_list.append(board[j][i])
        trans_board.append(trans_list[::-1])
    
    while True:
        
        delete_list = []
        for i in range(1,n):
            for j in range(1,m):
                two_by_two = list(set(trans_board[i-1][j-1:j+1] + trans_board[i][j-1:j+1]))
                
                if (len(two_by_two) == 1) and two_by_two[0].isalpha():
                    for location in [[i,j],[i,j-1],[i-1,j],[i-1,j-1]]:
                        if location not in delete_list:
                            delete_list.append(location)
        
        if delete_list:
            answer += len(delete_list)
        else:
            break

        for y,x in delete_list:
            trans_board[y][x] = '0'
        # 각 행의 숫자들을 뒤로빼고 글자를 앞으로 넣는 작업.
        for l in range(n):
            trans_board[l].sort(key = lambda x : 'a' if x.isalpha() else 'b')
        

        print(trans_board)
    return answer


board = ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']
m,n = 4,5

print(solution(m,n,board))