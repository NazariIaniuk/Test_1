import random
number=random.randint(1,5)
for i in range (1,5):
 ask=int(input('guess a number from 1 to 5'))
 if ask==number:
  print('Well done')
  break
 elif ask>number:
  print('too high, try again')
 elif ask<number:
  print('too low, try again')
if i <=2:
 print ('you win ')
else:
 print('you lose')