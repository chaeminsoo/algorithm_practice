from math import trunc
import random
import time

class person:
    def __init__(self, name, att, defence, dex, maxhp, pos):
        self.name = name
        self.att  = att
        self.defence = defence
        self.dex = dex
        self.maxhp = maxhp
        self.hp = maxhp

        total = 0
        for p in pos:
            total +=p
        self.pos = [p/total for p in pos]
        for i in range(1,len(self.pos)):
            self.pos[i] += self.pos[i-1]
    
    def print(self):
        print('[',self.name,']')
        print('체력:',int(self.hp),'/',self.maxhp)
        print('공방민:',self.att,self.defence, self.dex)

    def action_ai(self):
        p = random.random()

        if p> self.pos[1]:
           self.action = 2
           print(self.name,'회복 선택') 
        elif p > self.pos[0]:
            self.action = 1
            print(self.name,'크리티컬 공격 선택')
        else:
            self.action = 0
            print(self.name,'일반 공격 선택')
    
    def action_user(self,action):
        self.action = action

    def attack(self,target):

        if self.action == 2:
            self.hp += self.maxhp*0.1
            if self.hp > self.maxhp:
                self.hp = self.maxhp
        elif self.action ==1:
            rate = self.dex/(self.dex + target.dex)

            if random.random() < rate:
                damage = self.att*(100/(100+target.defence*0.5))*2
                target.hp -= damage
                print(self.name,'의 공격성공! 데미지',int(damage))
            else:
                print(self.name,'공격실패 ㅜㅜ')

        else:
            rate = (self.dex +50)/(self.dex + target.dex)

            if target.action ==2:
                rate=100

            if random.random() < rate:
                damage = self.att*(100/(100+target.defence))
                target.hp-=damage
                print(self.name,'의 공격성공! 데미지',int(damage))
            else:
                print(self.name,'공격실패 ㅜㅜ')

people = [
    person('honggildong',20,120,10,400,[50,10,40]),
    person('pikachu',40,10,100,200,[10,80,10]),
    person('majinga',60,60,60,1200,[30,30,40])
]

i = 1
for p in people:
    print(i,p.name)
    i+=1
print('select your char')
num = int(input()) -1
user = people[num]
print("select com's char")
num = int(input()) -1
target = people[num]

while True:
    user.print()
    time.sleep(0.5)
    target.print()
    time.sleep(0.5)
    print('1 일반공격, 2 크리티컬 공격, 3 회복')
    num = int(input()) -1
    user.action_user(num)
    target.action_ai()
    time.sleep(1)
    user.attack(target)
    if target.hp <=0:
        print(user.name,'win')
        break
    time.sleep(1)
    target.attack(user)
    if user.hp<=0:
        print(target.name,'win')
        break
    time.sleep(1)