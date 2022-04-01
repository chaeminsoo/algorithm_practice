# 1459
x,y,w,s = map(int,input().split())

diag_1 = True
diag_2 = False
if w*2 <= s:
    diag_1 = False
if w*2 >= s*2:
    diag_2 = True

if diag_1:
    ans = 0
    if x-y>=0:
        ans += s*y
        x-=y
        if diag_2:
            ans += ((x//2)*2)*s
            ans += (x%2)*w
        else:
            ans += x*w
    elif x-y<0:
        ans += s*x
        y-=x
        if diag_2:
            ans += ((y//2)*2)*s
            ans += (y%2)*w
        else:
            ans += y*w
    print(ans)
else:
    print((x+y)*w)