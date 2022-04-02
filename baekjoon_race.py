#1508
import heapq

n,m,k = map(int,input().split())
ref_location = list(map(int,input().split()))

interval_list = []
for i in range(0,k-1):
    heapq.heappush(interval_list,(ref_location[i+1] - ref_location[i],i))

for _ in range(k-m):
    heapq.heappop(interval_list)

print(interval_list)
# ans = ['0']*k
# while interval_list:
#     # ref = interval_list.pop()[1]
#     ref = heapq.heappop(interval_list)[1]
#     ans[ref] = '1'
#     ans[ref+1] = '1'

# print(''.join(ans))