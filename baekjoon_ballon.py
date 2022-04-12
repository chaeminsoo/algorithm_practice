#4716
while True:
    n,a,b = map(int,input().split())
    if n == 0 and a == 0 and b == 0:
        break
    teams = []
    ans = 0
    for _ in range(n):
        k_,da_,db_ = map(int,input().split())
        teams.append((k_,da_,db_))

    