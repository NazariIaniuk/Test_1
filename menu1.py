def f1(x,y):
  c=x+y
  return c
def f2(x,y):
   c=x-y
   return c
def ex(a=0):
   a=0
   return a
a=1
while a==1:
    ask=int(input('type 1 to add 2 number type 2 to subtract 2 numbers type 3 to exit'))
    if ask==1:
     x=int(input('enter a number you will add to '))
     y=int(input('enter a number you will add with'))
     print (f1(x,y))
    elif ask==2:
     x=int(input('enter a number you will subtract from'))
     y=int(input('enter another number you will subtract with'))
     print(f2(x,y))
    elif ask==3:
     a=ex
