n,m,k = map(int,input().split())
ref = []
ans = ''
for i in range(1,n+1):
    ref.append(str(i))
cursor_ = 0

def unit(ref,cur):
    ref1 = ref[cur]
    ref2 = ref[cur+1]
    ref3 = ref1+ref2
    del ref[cur]
    ref[cur] = ref3
    return

if n >= m+k-1:
    if n > m*k:
        print(-1)
    else:
        while len(ref) > m:
            if len(ref[cursor_]) < k:
                unit(ref,cursor_)
            else:
                cursor_ += 1
        for i in ref:
            j = i[::-1]
            ans+=j
        for k in ans:
            print(k,end=' ')
else:
    print(-1)