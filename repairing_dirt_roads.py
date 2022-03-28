#1911
from multiprocessing import pool


n, l = map(int,input().split())
pools_ = []
for _ in range(n):
    st,ed = map(int,input().split())
    pools_.append((st,ed))
pools_.sort()

cursor_ = pools_[0][0]
cnt = 0
for pool_ in pools_:
    pool_st,pool_ed = pool_

    if cursor_ >= pool_st and cursor_ <= pool_ed:
        while cursor_ >= pool_ed:
            cursor_ += l
            cnt += 1
    else:
        cursor_ = 