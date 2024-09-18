askup=input('do you want to count up or down?')
if askup=='up':
 number=int(input('what number do you want to count to?'))
 currentnumber=0
 while currentnumber<number:
     currentnumber+=1
     print(currentnumber)
elif askup=='down':
 number=int(input('enter a number below 20'))
 currentnumber=20
 while currentnumber>=number:
     print(currentnumber)
     currentnumber-=1
else:
 print('i do not understand')