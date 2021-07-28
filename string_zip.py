import time
st=time.time()

def solution(s):
    ref_result=[]
    result=''
    cnt=0
    for i in range(1,len(s)//2 +1):
        ref = s[:i]
        #result.append(ref)
        for j in range(i,len(s),i):
            check = s[j:j+i]
            #result+=check

            if ref == check:
                cnt+=1
                
            else:
                if cnt != 0:
                    ref = check
                    result+=str(cnt)
                    cnt=0
                
                result += ref
                ref = check
                
        ref_result.append(result)
    answer = ref_result
    return answer

'aabbacc'
print(solution('aabbacc'))
et=time.time()
print('time: ', et-st)