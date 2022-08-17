# 12904
s = input()
t = input()

while t != s:
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[:-1]
        t = t[::-1]
    
    if len(s) > len(t):
        break
if s == t:
    print(1)
else:
    print(0)