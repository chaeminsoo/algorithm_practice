#1802
t = int(input())

cases = []
for _ in range(t):
    a = input()
    cases.append(a)

def solution(target):
    stnd = int((len(target)-1)/2)
    ref_1 = target[:stnd]
    ref_2 = target[stnd+1:][::-1]
    ans = 'YES'
    for j in range(len(ref_1)):
        if int(ref_1[j]) + int(ref_2[j]) == 1:
            continue
        else:
            ans = 'NO'
            break
    return ans

for i in cases:
    print(solution(i))