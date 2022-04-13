#4716
while True:
    n,a,b = map(int,input().split())
    if n == 0 and a == 0 and b == 0:
        break
    teams = []
    ans = 0
    for _ in range(n):
        k_,da_,db_ = map(int,input().split())
        difference = abs(da_ - db_)
        teams.append((difference,k_,da_,db_))

    teams.sort()
    ans = 0
    for i in teams:
        dif,k,da,db = i
        if da >= db:
            if k <= b:
                b -= k
                ans += k*db
            else:
                ref = k - b
                ans += b*db
                ans += ref*da
        elif da < db:
            if k <= a:
                a -= k
                ans += k*da
            else:
                ref = k - a
                ans += a*da
                ans += ref*db
    print(ans)