def solution(food_times, k):
    
    while True:

        for i in range(len(food_times)):
            if food_times[i] > 0:
                food_times[i] -= 1
                k -= 1
            