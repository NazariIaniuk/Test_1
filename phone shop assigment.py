# funcions
def GBchoice(x=0):
 ask=int(input('''which storage option would you like?
              1) None $0
              2) 64 gigabytes $200
              3) 128 gigabytes $350    '''))
 if ask==1:
     return(0)
 elif ask==2:
   x=GB64()
   return(x)
 elif ask==3:
   x=GB128()
   return(x)
def GB64(x=0):
 x+=200
 return x
def GB128(x=0):
 x+=350
 return x
def dia(x=0):

   ask=input('would you like extra diamonds?')
   if ask=='y' or ask=='yes':
    x+=200
    return (x)
   elif ask=='n' or ask=='no':
     return(0)
def yearchoice(x=0):
  ask=int(input('''what cloud data option would you like?
                1) None $0
                2) 1 year $20
                3) 2 years $35 '''))
  if ask==1:
    return(0)
  elif ask==2:
    x=year1()
    return x
  elif ask==3:
    x=year2()
    return x
def year1(x=0):
   x+=20
   input('please enter your email.')
   return x
def year2(x=0):
   x+=35
   input('please enter your email')
   return x
def protrbr(x=0):
   x+=20
   return x
def protcarb(x=0):
   x+=100
   return x
def charg(x=0):
   ask=input('would you like a extra fast battery charger?')
   if ask=='n' or ask=='no':
    return (0)
   elif ask== 'y' or ask=='yes':    
    x+=100
   return x
def protchoice(x=0):
 protchoice=int(input('''wich protective case would you like?
   1) None $0
   2) Rubber $20
   3) Crbonfibre $100'''))
 if protchoice== 2:
    x=protrbr()
    return x
 elif protchoice == 3:
    x=protcarb()
    return x
 elif protchoice:
    return (0)
def choice_supressor(x=0):
  x=GBchoice()
  x+=yearchoice()
  x+=protchoice()
  x+=charg()
  return x
esc=0
while esc==0:
    total=0
    print('  welcome to phone shop.')
    package=int(input ('''  what package would you like to buy?
    1) McBasic Package
    2) Average JoePackage  
    3) Rich Kid ProPackage'''))
    if package==1:
       total+=50
       total+=protchoice()
       total+=charg()
       esc=1
    elif package==2:
       total+=150
       total+=choice_supressor()
       esc=1
    elif package==3:
       total+=800
       total+=dia()
       total+=choice_supressor()
       esc=1
print('your total is $',total)