def getRect(heights):
    
    if len(heights) == 1:
        return heights[0]
    
    mid = len(heights) // 2

    # left = getRect(heights[:mid])
    # right = getRect(heights[mid:])
    left = 9
    right = 12
    print(left,right)
    left_height, right_height = float('inf'), float('inf')
    
    left_right_wide, lr_width = 0,0
    l_idx, r_idx = mid-1, mid
    left_check, right_check = True, True
    while left_check or right_check:
        l_sum, r_sum = 0, 0
        lr_width += 1
        if left_check:
            left_height = min(left_height, heights[l_idx])
            l_sum = left_right_wide + left_height
        if right_check:
            right_height = min(right_height, heights[r_idx])
            r_sum = left_right_wide + right_height
        width = r_idx-l_idx+1
        left_right_wide = max(width*min(left_height,right_height), lr_width*max(left_height,right_height),left_right_wide)
        print(left_right_wide)
        
        if r_idx >= len(heights)-1:
            right_check = False
        else:
            r_idx += 1
        if l_idx <= 0:
            left_check = False
        else:
            l_idx -= 1
    return max([left, right, left_right_wide])

data = [4,3,1,2,3,4,4,3,1]

# print(getRect(data))
b = 'abc1'
b = b.rjust(5,'0')
print(b)
