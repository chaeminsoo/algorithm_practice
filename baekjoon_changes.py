#5585
n = int(input())
changes = 1000-n
cnt = 0

if changes//500 != 0:
    ref = (changes//500)
    changes -= ref*500
    cnt += ref
if changes//100 != 0:
    ref = (changes//100)
    changes -= ref*100
    cnt += ref
if changes//50 != 0:
    ref = (changes//50)
    changes -= ref*50
    cnt += ref
if changes//10 != 0:
    ref = (changes//10)
    changes -= ref*10
    cnt += ref
if changes//5 != 0:
    ref = (changes//5)
    changes -= ref*5
    cnt += ref
cnt += changes
print(cnt)