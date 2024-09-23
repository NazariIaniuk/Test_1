# if anything breaks it is because all the files are together and it has same variables, it should not happen as i tried to rename the variables by adding numbers

# for loop 3

maxnum=12
number=int(input('enter a number beteween 1 and 12'))
multiplicator=1
for i in range (0,maxnum):
 ans=number*multiplicator
 print(ans)
 multiplicator+=1

#for loop 5

total1=0
for i in range(0,5):
 num=int(input('enter a number'))
 ask=input('do you want the number included? type y to answer yes')
 if ask=='y':
     total1+=num
print(total1)

# while loop 1

total=0
while total<50:
 total+=int(input('input a number'))
 print('the total is', total)
 
# while loop 4

Name=input('who do you want to invite')
print(Name,'has been invited')
counter=1
ask1=input('do you want to invite another person? type y to agree')
while ask1=='y':
 Name=input('who do you want to invite')
 print(Name,'has been invited')
 counter+=1
 ask1=input('do you want to invite another person? type y to agree')
print ('you invited', counter,'people')

# loop 3

ask9=int(input('enter a strting number'))
for i in range(ask9,ask9+4):
    print (i)

#loop 6 

ask3=int(input('enter a  number'))
ask4=input('type y if you want to double the number')
ask3*=2
while ask4=='y':
 ask2=input('type y if you want to double the number')
 ask3*=2