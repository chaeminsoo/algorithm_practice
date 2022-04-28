n,k = map(int,input().split())
ref = input()
want_digit = n-k
ans = ''
cursor1 = 0
cursor2 = -want_digit
while cursor2 < 0:
    check_list = list(map(int,ref[cursor1:cursor2]))
    max_num = max(check_list)
    if max_num > int(ref[cursor2]):
        ans += str(max_num)
        idx = check_list.index(max_num)
        cursor1 = idx+1
        cursor2 +=1
    else:
        ans+=ref[cursor2:]
        break
print(int(ans))