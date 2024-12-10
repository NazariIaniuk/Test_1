import random
import csv
def test(x=0):
    global score
    score=0
    name=input('enter the user name')
    for i in range(0,5):
        a=random.randint(1,4)
        if a==1:
            A=random.randint(5,20)
            B=random.randint(5,20)
            x=A+B
            ans=int(input(f'enter the answer to this problem {A}+{B}:'))
            if ans==x:
                score+=1
        if a==2:
            A=random.randint(20,30)
            B=random.randint(10,20)
            x=A-B
            ans=int(input(f'enter the answer to this problem {A}-{B}:'))
            if ans==x:
                score+=1
        if a==3:
            A=random.choice([4,8,12,16,20,24,28])
            B=random.choice([2,4,8])
            x=A/B
            ans=int(input(f'enter the answer to this problem {A}/{B}:'))
            if ans==x:
                score+=1
        if a==4:
            A=random.randint(3,12)
            B=random.randint(3,12)
            x=A*B
            ans=int(input(f'enter the answer to this problem {A}*{B}:'))
            if ans==x:
                score+=1
    mathfile=open('mathsgame.csv','a')
    adddata=name+','+str(score)+',5'+','+str(score/5*100)+'%'+'\n'
    mathfile.write(str(adddata))
def viewdata(x=0):
    mathfile=open('mathsgame.csv','r')
    print(mathfile.read())
while True:
    menu=int(input(''' choose an action
                   1) Take the Quiz
                   2) Viev results
                   3) Exit'''))
    if menu==3:
        break
    elif menu==2:
        run=viewdata()
    elif menu==1:
        run=test()

