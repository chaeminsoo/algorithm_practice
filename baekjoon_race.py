#1508
from bisect import bisect_left

n,m,k = map(int,input().split())
ref_location = list(map(int,input().split()))

def bi_search(list_,interval_):
    cnt = 1
    st = list_[0]
    ed = list_[-1]
    ref = st
    while ref < ed:
        ref += interval_
        if cnt >= m:
            break
        if bisect_left(list_,ref) < k:
            cnt += 1
            continue
    if cnt >= m:
        return True
    else:
        return False

start_interval = 0
end_interval = n
mid_interval = (start_interval+end_interval)//2

while True:
    if mid_interval == start_interval or mid_interval == end_interval:
        break
    if bi_search(ref_location,mid_interval) == True:
        mid_interval = (mid_interval+end_interval)//2
    elif bi_search(ref_location,mid_interval) == False:
        mid_interval = (mid_interval+start_interval)//2

print(mid_interval)