# 1082
n = int(input())
p = list(map(int,input().split()))
m = int(input())
nums = []
ans = []
for i,j in enumerate(p):
    nums.append((i,j))
nums.sort(key= lambda x: (x[1],-x[0]))

ref_num, ref_cost = nums[0]
while True:
    if ans:
        if m >= ref_cost:
            m -= ref_cost
            ans.append(ref_num)
        else:
            break
    else:
        for i in nums:
            if i[0] != 0 and m >= i[1]:
                m -= i[1]
                ans.append(i[0])
                break
        for i in nums:
            if m >= i[1]:
                m -= i[1]
                ans.append(i[0])
                break
        

nums.sort(key= lambda x: (-x[0],x[1]))
la = len(ans)
cursor_ = 0
while m != 0:
    for num,cost in nums:
        if ans[cursor_] < num and (m+p[ans[cursor_]]) >= cost:
            m += p[ans[cursor_]]
            m -= cost
            ans[cursor_] = num
            break
    cursor_+=1
    if cursor_ == la:
        break
rslt = ''
for i in ans:
    rslt+=str(i)
print(int(rslt))