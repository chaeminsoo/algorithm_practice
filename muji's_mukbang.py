import heapq

def solution(food_times, k):
    
    if sum(food_times) <=k:
        return -1
    
    foods=[]
    leng = len(food_times)
        
    for i in range(leng):
        heapq.heappush(foods,[food_times[i],i+1])
    
    ref_num=0
    ref_k = k
    while foods:
        ref_num+=foods[0][0]
        ref_k -= foods[0][0]*len(foods)
        
        if ref_k<=0:
            break
        else:
            heapq.heappop(foods)
            foods[0][0] -= ref_num
            k = ref_k

    address=k%len(foods)
    
    foods.sort(key=lambda x:x[1])
    
    
    answer = foods[address][1]
          
    
    return answer