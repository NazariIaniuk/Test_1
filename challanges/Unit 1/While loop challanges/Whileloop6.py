number=int(input('guess the number'))
while number<10 or number>20:
 if number<10:
     print('too low' )
     number=int(input('try again'))
 elif number>20:
     print('too high')
     number=int(input('try again'))
print('thank you')