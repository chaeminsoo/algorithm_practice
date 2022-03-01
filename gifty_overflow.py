n = int(input())
due = list(map(int,input().split()))
plan = list(map(int,input().split()))
gift_order = []

for i in range(n):
    gift_order.append([i,plan[i]])

gift_order.sort(key= lambda x:x[1])
for i in range(n):
    ref = gift_order[i][1]
    for j in range(i+1,n):
        gift_order[j][1] -= ref
cnt = 0

def day_goes(day):
    for i in range(n):
        if type(due[i]) == str:
            continue
        elif type(due[i]) == int:
            due[i] -= day

def extend(target):
    global cnt
    while due[target] < 0:
        due[target] += 30
        cnt += 1
    for i in range(n):
        if plan[i] == plan[target]: 
            continue
        if type(due[i]) == str:
            continue
        elif type(due[i]) == int:
            while due[i] < due[target]:
                due[i] += 30
                cnt +=1

for must_use in gift_order:
    num, day = must_use
    day_goes(day)
    extend(num)
    due[num] = 'x'
    # due[num] = 1e10

print(cnt)