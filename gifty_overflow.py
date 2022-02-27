n = int(input())
due = list(map(int,input().split()))
plan = list(map(int,input().split()))

cnt = 0
last_day = max(plan)

def solution(gift_num):
    return

for today in range(1,last_day+1):
    for i in range(len(due)):
        due[i] -= 1
        if due[i] == 0:
            due[i] = 30
            cnt += 1
    
    if today not in plan:
        continue

    while True:
        try:
            gifty_num = plan.index(today)
        except ValueError:
            break
        
        if due[gifty_num] != min(due):
            continue

        due[gifty_num] = 1e9

print(cnt)