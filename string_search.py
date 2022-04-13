#1543
stnd = input()
target = input()
s_len = len(stnd)
t_len = len(target)

cursor_ = 0
cnt = 0
while cursor_ + t_len <= s_len:
    if stnd[cursor_:cursor_+t_len] == target:
        cursor_ += t_len
        cnt += 1
    else:
        cursor_ += 1

print(cnt)