n = int(input())

field =[]
blanks = 0

for _ in range(n):
    row = list(input().split())
    for i in row:
        if i == 'X':
            blanks+=1
    field.append(row)

stop_num = (blanks*(blanks-1)*(blanks-2))/6

def check():
    result = False
    a
    return result

def set_obj(field):
    if check:
        return

print(blanks)