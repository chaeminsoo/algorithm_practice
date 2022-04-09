#1802
def solution(target):
    if len(target) == 1:
        return 'YES'
    stnd = int((len(target)-1)/2)
    ref_1 = target[:stnd]
    ref_2 = target[stnd+1:][::-1]
    for j in range(len(ref_1)):
        if int(ref_1[j]) + int(ref_2[j]) == 1:
            continue
        else:
            return 'NO'
    return solution(ref_1)


for tc in range(int(input())):
    print(solution(input()))