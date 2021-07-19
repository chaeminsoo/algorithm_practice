n = input()

cnt=2
result = 0

if int(n[0]) == 0 or int(n[1]) == 0:
    result += int(n[0])+int(n[1])
else:
    result += int(n[0])*int(n[1])


while cnt < len(n):
    
    if n[cnt] ==0:
        cnt+=1
        continue
    else:
        result *= int(n[cnt])
        cnt+=1
        continue

print(result)