# 1459
x,y,w,s = map(int,input().split())

diag_ = True
if w*2 <= s:
    diag_ = False

if diag_:
    ans = 0
    if x-y>=0:
        ans += s*y
        x-=y
        if x%2 == 0:
            ans += s*x
        else:
            ans += s*(x-1)
            ans += w
    print(ans)
else:
    print((x+y)*w)