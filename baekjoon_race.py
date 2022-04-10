#1508
from bisect import bisect_left

n,m,k = map(int,input().split())
ref_location = list(map(int,input().split()))

def bi_search(list_,interval_):
    cnt = 1
    ref = list_[0]
    for i in range(1,len(list_)):
        if list_[i] >= ref + interval_:
            cnt += 1
            ref += interval_
        else:
            continue
    if cnt >= m:
        print('===',cnt)
        return True
    else:
        return False

st = 0
ed = n
mid = (st+ed)//2

while st != mid:
    if bi_search(ref_location,mid):
        st = mid
        mid = (st+ed)//2
    else:
        ed = mid
        mid = (st+ed)//2
        
print(mid)