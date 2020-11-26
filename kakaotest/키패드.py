def solution(numbers,hand):
    
    answer = ""
    keypad = [[1,4,7,'*'],[2,5,8,0],[3,6,9,'#']]

    left = [0,3]
    right =[2,3]
    for number in numbers:
        if number in keypad[0]:
            answer += 'L'
            left = [0,keypad[0].index(number)]
        elif number in keypad[2]:
            answer += 'R'
            right = [2,keypad[2].index(number)]
        else:
            want = [1,keypad[1].index(number)]
            left_want = abs(left[0]-want[0]+left[1]-want[1])
            right_want = abs(right[0]-want[0] + right[1] - want[1])
            if right_want < left_want:
                answer += 'R'
                right = want
            elif right_want > left_want:
                answer += 'L'
                left = want
            else:
                if hand == 'right':
                    answer += 'R'
                    right = want
                else:
                    answer += 'L'
                    left = want
    
    return answer