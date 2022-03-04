n = int(input())
due_data = list(map(int,input().split()))
plan_data = list(map(int,input().split()))
#-------------------------------------------------
gifty = []
for i in range(n):
    gifty.append([plan_data[i],due_data[i]])
gifty.sort()

cnt = 0

section = gifty[0][0]
section_max = 0
pre_section_max = 0
ref = []

for gift in gifty:
    plan, due = gift
    if plan != section:
        section = plan
        pre_section_max = max(ref)
        print('====',pre_section_max)
        ref.clear()
        if due < section:
            share = (section-due)//30
            due += (share+1)*30
            cnt+=(share)
        if due < pre_section_max:
            share = (pre_section_max-due)//30
            due += (share+1)*30
            cnt+=(share)
        ref.append(due)
    else:
        if due < section:
            share = (section-due)//30
            due += (share+1)*30
            cnt+=(share)
        if due < pre_section_max:
            share = (pre_section_max-due)//30
            due += (share+1)*30
            cnt+=(share)
        ref.append(due)

print(cnt)


#--------------------------------------------------
# gifty = []
# for i in range(n):
#     gifty.append([plan_data[i],due_data[i]])
# gifty.sort()

# cursor_ = 0
# def find_section(gifty,cursor_):
#     ref = -1
#     standard = gifty[cursor_][0]
#     for i in range(cursor_,n):
#         if gifty[i][0] == standard:
#             ref += 1
#         else:
#             break
#     return ref+cursor_
# sections = []
# while True:
#     try:
#         ref = find_section(gifty,cursor_)
#     except IndexError:
#         break
#     sections.append((cursor_,ref))
#     cursor_ = ref+1

# cnt=0
# pre_max = gifty[0][0]
# for section in sections:
#     st, en = section
#     standard = gifty[st][0]
#     section_max = standard
#     for num in range(st,en+1):
#         while gifty[num][1] < pre_max:
#             gifty[num][1] += 30
#             cnt+=1
#         while gifty[num][1] < standard:
#             gifty[num][1] += 30
#             cnt+=1
#         section_max = max(section_max,gifty[num][1])
#     pre_max = section_max
    
# print(cnt)

        

#---------------------------------------------------
# gift_order = []

# for i in range(n):
#     gift_order.append([i,plan[i]])

# gift_order.sort(key= lambda x:x[1])
# for i in range(n):
#     ref = gift_order[i][1]
#     for j in range(i+1,n):
#         gift_order[j][1] -= ref
# cnt = 0

# def day_goes(day):
#     for i in range(n):
#         if type(due[i]) == str:
#             continue
#         elif type(due[i]) == int:
#             due[i] -= day

# def extend(target):
#     global cnt
#     while due[target] < 0:
#         due[target] += 30
#         cnt += 1
#     for i in range(n):
#         if plan[i] == plan[target]: 
#             continue
#         if type(due[i]) == str:
#             continue
#         elif type(due[i]) == int:
#             while due[i] < due[target]:
#                 due[i] += 30
#                 cnt +=1

# for must_use in gift_order:
#     num, day = must_use
#     day_goes(day)
#     extend(num)
#     due[num] = 'x'
#     # due[num] = 1e10

# print(cnt)