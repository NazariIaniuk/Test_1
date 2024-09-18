number=int(input('enter a number'))
number2=int(input('enter another number'))
total=number+number2
answer=input('if you want tot enter another number type y')
while answer=='y':
 total+=int(input('enter a number you want to add'))
 answer=input('if you want tot enter another number type y')
print(total)
