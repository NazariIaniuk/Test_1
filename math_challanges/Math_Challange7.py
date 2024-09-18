# you can modify maxinputnumber to properly find factors of higher numbers
A=int(input('input the number you want to find factors of, if the number is higer than 20 it may not find all factors of it '))
B=1
maxinputnumber=20
while maxinputnumber>0:
 C=(A/B)
 D=A//B
 if C==D:
     print(D,'is a factor of',A)
     maxinputnumber-=1
     B+=1
 else:
     maxinputnumber-=1
     B+=1
