def f1(x,y):
  c=x+y
  return c
def f2(x,y):
   c=x-y
   return c
def ex(a=0):
   a=True
   return a
a=True
while a==True:
    print ('''menu
           1) add rwo number
           2) subtract two number
           3) exit''')
    ask=int(input('select option'))
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
