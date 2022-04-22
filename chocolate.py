#2885
k = int(input())

def find_n(kk):
    a = 0
    while 2**a <kk:
        a+=1
    return 2**a,a

n,a = find_n(k)
b_k = format(k,'b')
lenbn = len(b_k)
ans = a
for i in range(lenbn-1,-1,-1):
    check_ = b_k[i]
    if check_ == '1':
        break
    else:
        ans-=1
print(n,ans)