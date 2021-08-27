from itertools import permutations

def close_num(target,liist):
    ref = 0
    for i in liist:
        if i >= target:
            ref = i
            break
    return ref

def solution(n, weak, dist):
    wl = len(weak)
    new_weak = weak + [i + n for i in weak]
    min_cnt = 100#float('inf')
    all_cases = list(permutations(dist,len(dist)))
    for sp in weak:
        for case in all_cases:
            wp = sp
            cnt = 0
            weak_cnt = 0
            for friend in case:
                arrived = wp +friend

                for i in new_weak:
                    if i >= wp and i <= arrived:
                        weak_cnt +=1
                cnt += 1
                if weak_cnt >= wl:
                    min_cnt = min(min_cnt,cnt)
                    break
                else:
                    wp  = close_num(arrived,weak)
                    # if wp == 0:
                    #     break
                    # # print(wp)##
    
    if min_cnt > 8:#== float('inf'):
        answer = -1
    else:
        answer = min_cnt
        
    return answer
#-------------------------------------------------------------

print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4])) # 2
print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7])) # 1
print(solution(12,[1, 3, 4, 9, 10],[1,3])) # 2 안나옴
print(solution(12,[1, 3, 4, 9, 10],[1,1,1])) # 3
print(solution(12,[1,2,5,6,9,10],[1,1,1])) # 3 안나옴
print(solution(12,[1,2,4,5],[1,1])) # 1 안나옴
