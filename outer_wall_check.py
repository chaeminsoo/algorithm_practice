def check(dist,weak,all_weak):
    long_d = dist.pop()
    ref_list=[]
    for wp in weak:
        chosen_wp =[]
        cw = wp + long_d
        ccw = wp - long_d
        cw_list=[]
        ccw_list=[]
        for i in range(wp,cw+1):
            if i in all_weak:
                cw_list.append(i)
        for i in range(ccw,wp+1):
            if i in all_weak:
                ccw_list.append(i)
        
        if len(cw_list) >= len(ccw_list):
            chosen_wp = cw_list
        else:
            chosen_wp = ccw_list
        chosen_wp.sort()
        if len(chosen_wp) > len(ref_list):
            ref_list = chosen_wp
        elif len(chosen_wp) == len(ref_list):
            rf_f, rf_l = ref_list[0],ref_list[-1]
            c_f,c_l = chosen_wp[0], chosen_wp[-1]
            if (rf_l - rf_f) >= (c_l - c_f):
                pass
            else:
                ref_list = chosen_wp



def solution(n, weak, dist):
    answer = 0
    dist.sort()
    past_weak = []
    next_weak=[]
    for i in weak:
        past_weak.append(i-n)
        next_weak.append(i+n)
    all_weak = past_weak + weak + next_weak
    
    
    return answer