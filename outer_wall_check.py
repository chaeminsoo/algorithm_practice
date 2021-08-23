def check(weak,dist,new_weak,n,cnt):
    chosen = []
    for wp in weak:
        friend = dist[-1]
        covered = []
        for i in range(wp,wp+friend+1):
            if i in new_weak:
                covered.append(i)
        if len(chosen) < len(covered):
            chosen = covered
    # chosen is confirmed
    for i in chosen:
        if i >= n:
            i-=n
        if i in weak:
            weak.remove(i)
    dist.pop()
    cnt+=1
    

def solution(n, weak, dist):
    answer = 0
    dist.sort()
    new_weak=[]
    for i in weak:
        new_weak.append(i)
        new_weak.append(i+n)
    new_weak.sort()
    # #----------------------------------------------------------
    # cnt=0
    # chosen = []
    # for wp in weak:
    #     friend = dist[-1]
    #     covered = []
    #     for i in range(wp,wp+friend+1):
    #         if i in new_weak:
    #             covered.append(i)
    #     if len(chosen) < len(covered):
    #         chosen = covered
    # # chosen is confirmed
    # for i in chosen:
    #     if i >= n:
    #         i-=n
    #     weak.remove(i)
    # cnt+=1
    # # one down ---------------
    cnt = 0
    while weak:
        try:
            check(weak,dist,new_weak,n,cnt)
        except IndexError:
            answer = -1
            break
    answer = cnt        
    return answer