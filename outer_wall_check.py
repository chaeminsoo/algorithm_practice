# # 1st try
# def check(weak,dist,new_weak,n,a):
#     chosen = []
#     for wp in weak:
#         friend = dist[a]
#         covered = []
#         for i in range(wp,wp+friend+1):
#             if i in new_weak:
#                 covered.append(i)
#         if len(chosen) < len(covered):
#             chosen = covered
    
#     for i in chosen:
#         if i >= n:
#             i-=n
#         if i in weak:
#             weak.remove(i)
#     a-=1
#     return 1
    

# def solution(n, weak, dist):
#     answer = 0
#     dist.sort()
#     new_weak=[]
#     a=-1
#     for i in weak:
#         new_weak.append(i)
#         new_weak.append(i+n)
#     new_weak.sort()
#     while weak:
#         try:
#             answer += check(weak,dist,new_weak,n,a)
#         except IndexError:
#             answer = -1
#             break
#     return answer
    
# print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4])) # 2
# print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7])) # 1
#-----------------------------------------------------------------------------------------------------------------------------------------
from itertools import permutations

def close_num(targrt,liist):
    ref = []
    for i in range(len(liist)):
        val = liist[i]
        distance = abs(targrt-val)
        ref.append((distance,i))
    ref.sort()
    return liist[ref[0][1]]

def solution(n, weak, dist):
    answer = 0
    new_weak = []
    for i in weak:
        new_weak.append(i)
        new_weak.append(i+n)
    new_weak.sort()

    Xs = permutations(dist,len(dist))
    min_cnt = float('INF')
    for sp in weak:
        for x in Xs:
            cnt = 1
            # f_cnt = 0
            check =[]
            for j in range(len(x)):#while cnt < len(dist):
                friend = x[j]
                # try:
                #     friend = x[f_cnt]
                # except IndexError:
                #     break

                for k in range(sp,sp+friend+1):
                    if k in new_weak:
                        if k >= n: k -= n
                        check.append(k)
                check = list(set(check))
                # cnt = j
                # # f_cnt+=1
                check.sort()
                if check == weak:
                    break
                else:
                    cnt +=1
                    sp = close_num(sp+friend,weak)
                min_cnt = min(min_cnt,cnt)
    
    # if min_cnt > len(dist):
    #     answer = -1
    # else:
    answer = min_cnt

    return answer

print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4])) # 2
print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7])) # 1