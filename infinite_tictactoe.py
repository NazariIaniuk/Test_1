pA1=' '
pA2=' '
pA3=' '
pB1=' '
pB2=' '
pB3=' '
pC1=' '
pC2=' '
pC3=' '
def tilechangex(x=0):
 ask=input('which tile would you like to change to x')
 global pA1
 global pA2
 global pA3
 global pB1 
 global pB2
 global pB3
 global pC1
 global pC2
 global pC3
 if ask=='A1':
   pA1='X'
 elif ask=='A2':
   pA2='X'
 elif ask=='A3':
   pA3='X'
 elif ask=='B1':
   pB1='X'
 elif ask=='B2':
   pB2='X'
 elif ask=='B3':
   pB3='X'
 elif ask=='C1':
  pC1='X'
 elif ask=='C2':
  pC2='X'
 elif ask=='C3':
  pC3='X'
 print ('   1   2   3')
 print ('A|',pA1,'|',pA2,'|',pA3,'|')
 print ('B|',pB1,'|',pB2,'|',pB3,'|')
 print ('C|',pC1,'|',pC2,'|',pC3,'|')
 print ('   1   2   3')
def tilechangeo(x=0):
 
 ask=input('which tile would you like to change to o')
 global pA1
 global pA2
 global pA3
 global pB1 
 global pB2
 global pB3
 global pC1
 global pC2
 global pC3
 if ask=='A1':
   pA1='O'
 elif ask=='A2':
   pA2='O'
 elif ask=='A3':
   pA3='O'
 elif ask=='B1':
   pB1='O'
 elif ask=='B2':
   pB2='O'
 elif ask=='B3':
   pB3='O'
 elif ask=='C1':
   pC1='O'
 elif ask=='C2':
   pC2='o'
 elif ask=='C3':
   pC3='O'
 print ('   1   2   3')
 print ('A|',pA1,'|',pA2,'|',pA3,'|')
 print ('B|',pB1,'|',pB2,'|',pB3,'|')
 print ('C|',pC1,'|',pC2,'|',pC3,'|')
 print ('   1   2   3')
def boardpprint (x=0):
 
 print ('A|',pA1,'|',pA2,'|',pA3,'|')
 print ('B|',pB1,'|',pB2,'|',pB3,'|')
 print ('C|',pC1,'|',pC2,'|',pC3,'|')
print('in infinite tic tac toe your pieces will dissapear and you can only have 3 at a time')