def solution(key, lock):
    answer = False
    
    m =len(key)
    n = len(lock)
    offset =  m-1
    new_len = offset*2 +n
    moving = offset+n
    
    new_lock = [[0]*new_len for _ in range(new_len)]
    
    
    for i in range(n):
        for j in range(n):
            new_lock[i+offset][j+offset] = lock[i][j] 
    
    for i in range(moving):
        for j in range(moving):
            for rrot in range(4):
                ref_key = rot_90(key)
                
                for k in range(m):
                    for l in range(m):
                        new_lock[k+i][l+j] += ref_key[k][l]

                if check(new_lock, offset,n) == True:
                    answer = True
                    break
                else:
                    for k in range(m):
                        for l in range(m):
                            new_lock[k+i][l+j] -= key[k][l]
                    
                    key = ref_key
                    
        if answer == True:
            break
    
    return answer

def check(new_lock,offset,n):
    result = True
    for i in range(n):
        for j in range(n):
            if new_lock[i+offset][j+offset] != 1:
                result = False
                break
        if result == False:
            break
    return result

def rot_90(a):
    n=len(a)
    m=len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]            
    return result
    
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))