import random
score=0
a=random.randint(3,15)
b=random.randint(5,25)
c=random.randint(4,5)
d=random.randint(3,11)
e=random.randint(1,13)
f=random.randint(3,11)
g=random.randint(2,14)
h=random.randint(0,15)
i=random.randint(2,4)
j=random.randint(2,4)
print ('question 1')
ask1=int(input(f'what is the answer to {a}+{b}?'))
ans1=a+b
if ans1==ask1:
 score+=1
 print ('question 2')
ask1=int(input(f'what is the answer to {c}*{d}?'))
ans1=c*d
if ans1==ask1:
 score+=1
 print ('question 3')
ask1=int(input(f'what is the answer to {e}-{f}?'))
ans1=e-f
if ans1==ask1:
 score+=1
 print ('question 4')
ask1=int(input(f'what is the answer to {g}*{h}?'))
ans1=g*h
if ans1==ask1:
 score+=1
 print ('question 5')
ask1=int(input(f'what is the answer to {i}^{j}?'))
ans1=i**j
if ans1==ask1:
 score+=1
print(f'your score is {score} out of 5')