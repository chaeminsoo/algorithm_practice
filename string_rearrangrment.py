string = input()

alpha=[]
num=[]

for i in string:
    try:
        num.append(int(i))
    except  ValueError:
        alpha.append(i)

alpha.sort()
result=''

for i in alpha:
    result+=i

print(result, end='')
print(sum(num))