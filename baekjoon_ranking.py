#2012
import sys
input = sys.stdin.readline

n = int(input())
pred_rank = []
for _ in range(n):
    pred_rank.append(int(input()))

pred_rank.sort()
ans = 0
for i,j in enumerate(pred_rank):
    ans += abs((i+1)-j)
print(ans)