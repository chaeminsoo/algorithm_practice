def count_w(wp,cw,ccw,all_weak):
    c_weak=[]
    cc_weak=[]
    for i in range(wp,cw+1):
        if i in all_weak:
            c_weak.append(i)
    for i in range(ccw,wp+1):
        if i in all_weak:
            cc_weak.append(i)
            
    if len(c_weak) >= len(cc_weak):
        c_weak.sort()
        return c_weak
    else:
        cc_weak.sort()
        return cc_weak

def check(weak,dist,all_weak,n):
    long_d = dist.pop()
    ref_list = []
    if long_d >= n:
        return 'end'
    
    for wp in weak:
        cw = wp + long_d
        ccw = wp - long_d
        
        ref = count_w(wp,cw,ccw,all_weak)
        
        if len(ref_list) < len(ref):
            ref_list = ref
        elif len(ref_list) == len(ref):
            rl_value = ref_list[-1] - ref_list[0]
            r_value = ref[-1] - ref[0]
            if rl_value >= r_value:
                ref_list = ref_list
            else:
                ref_list = ref
        else: continue
    for i in ref_list:
        weak.remove(i)
    
def solution(n, weak, dist):
    answer = 0
    able = True
    dist.sort()
    past_weak = []
    next_weak=[]
    for i in weak:
        past_weak.append(i-n)
        next_weak.append(i+n)
    all_weak = past_weak + weak + next_weak
    
    while weak:
        check(weak,dist,all_weak,n)
        answer +=1
        if dist:
            continue
        else:
            able = False
            break
    
    if able:
        return answer
    else:
        return -1