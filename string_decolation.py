#1294
n = int(input())
str_list = []
for _ in range(n):
    str_list.append(input())
real_list = [[] for _ in range(n)]
total_latter = 0
for i in range(n):
    for j in str_list[i]:
        real_list[i].append(j)
        total_latter+=1
        
cnt = [0]*n
ans = ''
while sum(cnt) < total_latter-n:
    ref = []
    # try:
    for k,l in enumerate(cnt):
        ref.append((real_list[k][l],k))
    # except IndexError:
    #     pass
    #     # print('==',k)
    #     # print('++',l)
    #     # break
    ref.sort()
    ref_value = ref[0]
    ans+=ref_value[0]
    cnt[ref_value[1]]+=1
    if cnt[ref_value[1]] >= len(str_list[ref_value[1]]):
        cnt[ref_value[1]]-=1

print(ans)