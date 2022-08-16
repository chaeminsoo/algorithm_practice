# 17609
t = int(input())
def checking(s,cnt):
    ls = len(s)-1
    cursor1 = 0
    cursor2 = ls
    while cursor1 < cursor2:
        if s[cursor1] == s[cursor2]:
            cursor1+=1
            cursor2-=1
        else:
            if cnt >= 1:
                return 2
            else:
                ref1 = checking(s[:cursor1]+s[cursor1+1:],cnt+1)
                ref2 = checking(s[:cursor2]+s[cursor2+1:],cnt+1)
                if ref1 == 0 or ref2 == 0:
                    return 1
                else:
                    return 2
    return 0

for _ in range(t):
    data = input()
    print(checking(data,0))