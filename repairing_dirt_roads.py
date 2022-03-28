#1911
from multiprocessing import pool


n, l = map(int,input().split())
pool_ = []
for _ in range(n):
    st,ed = map(int,input().split())
    pool_.append((st,ed))
pool_.sort()
print(pool_)