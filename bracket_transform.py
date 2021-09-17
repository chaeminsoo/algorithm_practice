def check(p):
    stack=[]
    for i in p:
        if len(stack)==0:
            if string=='(':
                stack.append(string)
            else:
                return False
        
        if string=='(':
            stack.append(string)
        elif string==')':
            stack.pop()
    
    if len(stack)==0:
        return True
    return False

def divide(p):
    r=0
    l=0
    for i in q:
        if i == '(':
            r+=1
        else i == ')':
            l+=1
        if r == l:
            break
    return r+l-1

def solution(p):
    answer = ''
    if check(p):
        return p
    else:
        divide(p) = num
        
    return answer