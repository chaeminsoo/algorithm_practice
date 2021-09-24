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
    min_cnt = 1e9
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
                    wp  = close_num(arrived+1,new_weak) 
    
    if min_cnt > 8: 
        return -1
    else:
        return min_cnt