compnum=50
guess=int(input('guess the number'))
attempt=1
while compnum!=guess:
 if guess<compnum:
     attempt+=1
     print('go higher')
     guess=int(input('guess the number'))
 elif guess>compnum:
     attempt+=1
     print('go lower')
     guess=int(input('guess the number'))
print('congratulations it tooks you',attempt,'attmepts')