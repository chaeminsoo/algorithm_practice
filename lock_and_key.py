import copy

def solution(key, lock):
    answer = True
    
    n=len(lock)
    m=len(key)
    
    new_lock = [[0]*(2*m+(n-2)) for _ in range(2*m+(n-2))]
    
    for i in range(n):
        for j in range(n):
            new_lock[(m-1)+i][(m-1)+j] = lock[i][j]
    
    ref_lock = copy.deepcopy(new_lock)
    
    area = n+(m-1)
    
    for i in range(area):
        for j in range(area):
            
            
    
        
                    
    return answer

def turn_90(a):
    n=len(a)
    m=len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

def check(a,k):
    result = True
    n=len(a)
    m=len(k)
    for i in range(m-1,m-1+n,1):
        for j in range(m-1,m-1+n,1):
            if a[i][j] != 1:
                result = False
                break
        if result == False:
            break
    return result