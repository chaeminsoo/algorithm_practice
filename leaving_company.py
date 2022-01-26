n = int(input())
schedule = [0]
pay_check = [0]
for i in range(n):
    t,p = map(int,input().split())
    pay_check.append(p)
    schedule.append(t)

next_schedule = [[] for _ in range(n+1)]
before_schedule = [[] for _ in range(n+1)]

def checking(day):
    date,t = day
    for i in range(date+t,n+1):
        if schedule[i]+i <= n+1:
            next_schedule[date].append(i)

for i in range(1,len(schedule)):
    checking((i,schedule[i]))

for j in range(len(next_schedule)):
    if next_schedule[j]:
        for k in next_schedule[j]:
            before_schedule[k].append(j)

answer = [0 for _ in range(n+1)]

def paying(day):
    ref = []
    if before_schedule[day]:
        for i in before_schedule[day]:
            ref.append(pay_check[i])
        return max(ref)
    else:
        return 0

for l in range(1,n+1):
    pay_check[l]+=paying(l)
    if l + schedule[l] >n+1:
        pay_check[l]*=0

print(max(pay_check))