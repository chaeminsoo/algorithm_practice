# 1202
import sys

input = sys.stdin.readline
n,k = map(int,input().split())

def bi_search(target,s,e,list_):
    mid = (s+e)//2
    if mid == s:
        return mid
    if list_[mid] == target:
        return mid
    elif list_[mid] < target:
        return bi_search(target,mid,e,list_)
    elif list_[mid] > target:
        return bi_search(target,s,mid,list_)

jewel = []
bag = []
for _ in range(n):
    m,v = map(int,input().split())
    jewel.append((m,v))
for _ in range(k):
    c = int(input())
    bag.append(c)
    
jewel.sort(key= lambda x:(-x[1],x[0]))
bag.sort()
ans = 0

for weight, val in jewel:
    if k==0: break
    ref_idx = bi_search(weight,0,k-1,bag)
    
    if bag[ref_idx] == weight:
        bag.pop(ref_idx)
        ans += val
        k -= 1
    elif bag[ref_idx] < weight:
        try:
            bag.pop(ref_idx+1)
            ans += val
            k -= 1
        except IndexError:
            continue
    elif bag[ref_idx] > weight:
        bag.pop(ref_idx)
        ans += val
        k -= 1

print(ans)