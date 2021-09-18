def check(p):
    stack=[]
    
    for i in p:
        if len(stack) ==0 and i ==')':
            return False
        
        if i =='(':
            stack.append(i)
        elif i ==')':
            stack.pop()
    if len(stack) != 0:
        return False
    else:
        return True
    
def change(sss):
    result =''
    for i in sss:
        if i =='(':
            result+=')'
        elif i == ')':
            result+='('
    return result

def cut(string):
    o=0
    c=0
    for i in range(len(string)):
        if string[i] == '(':
            o+=1
        elif string[i] == ")":
            c+=1
        
        if o == c:
            return i+1

def transform(string):
    if check(string) or string == '':
        return string

    result=''
    num = cut(string)
    u = string[:num]
    v = string[num:]
    if check(u):
        return u + transform(v)
    else:
        result+='(' + transform(v) + ')' + change(u[1:-1])
        return result
        
def solution(p):
    if p == '':
        return ''
    
    if check(p):
        return p
    else:
        return transform(p)