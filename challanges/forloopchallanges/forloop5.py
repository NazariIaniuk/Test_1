total=0
for i in range(0,5):
 num=int(input('enter a number'))
 ask=input('do you want the number included? type y to answer yes')
 if ask=='y':
     total+=num
print(total)