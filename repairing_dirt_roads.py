#1911
import math

n, l = map(int,input().split())
pools_ = []
for _ in range(n):
    st,ed = map(int,input().split())
    pools_.append((st,ed))
pools_.sort()

cursor_ = pools_[0][0]
cnt = 0
for pool_st, pool_ed in pools_:
    if cursor_ < pool_st:
        cursor_ = pool_st
    while cursor_ < pool_ed:
        ref = math.ceil((pool_ed - cursor_)/l)
        cursor_ += ref*l
        cnt += ref
print(cnt)