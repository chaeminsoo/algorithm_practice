def solution(food_times, k):
    answer = 0
    cnt = 0
    
    
    for index in range(len(food_times)):
        
        if food_times[index] ==0:
            continue
        else:
            food_times[index] = food_times[index] -1
            cnt +=1
            
                       
    
    return answer

if __name__ == '__main__':
    solution([3,1,2],5)