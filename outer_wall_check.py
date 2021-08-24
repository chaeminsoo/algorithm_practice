def check(weak,dist,new_weak,n,a):
    chosen = []
    for wp in weak:
        friend = dist[a]#-1]
        covered = []
        for i in range(wp,wp+friend+1):
            if i in new_weak:
                covered.append(i)
        if len(chosen) < len(covered):
            chosen = covered
        # elif len(chosen) == len(covered):
            # ref_cho , ref_cov = weak,weak
            # for i in chosen:
            #     if i >= n:
            #         i-=n
            #     if i in weak:
            #         ref_cho.remove(i)
            # for i in covered:
            #     if i >= n:
            #         i-=n
            #     if i in weak:
            #         ref_cov.remove(i)

            # aaa = solution(n, chosen, dist)
            # bbb = solution(n, covered, dist)
            
            # if aaa >= bbb:
            #     chosen = covered
            # else:
            #     pass

    # chosen is confirmed
    for i in chosen:
        if i >= n:
            i-=n
        if i in weak:
            weak.remove(i)
    #dist.pop()
    a-=1
    # #--
    return 1
    

def solution(n, weak, dist):
    answer = 0
    dist.sort()
    new_weak=[]
    a=-1
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
    while weak:
        try:
            answer += check(weak,dist,new_weak,n,a)
        except IndexError:
            answer = -1
            break
    return answer
    

print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))
print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7]))