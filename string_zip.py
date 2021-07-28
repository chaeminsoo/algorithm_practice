from collections import deque
import re

def solution(s):
    leng = len(s)
    answer = leng
    for i in range(1,leng//2+1):
        cut_list = re.sub('(\w{%i})' %i, '\g<1> ',s).split()
        q=deque(cut_list)
        result=''
        ref = q.popleft()
        num_cnt=1
        
        while q:
            check = q.popleft()
            if ref == check:
                num_cnt+=1
            else:
                if num_cnt !=1:
                    result+=str(num_cnt)
                    num_cnt=1
                result+=ref
                ref=check
        if num_cnt !=1:
            result+=str(num_cnt)
        result+=ref

        answer = min(answer,len(result))
                
            
    return answer

'aabbacc'
print(solution('aabbacc'))