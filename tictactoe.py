pA1=' '
pA2=' '
pA3=' '
pB1=' '
pB2=' '
pB3=' '
pC1=' '
pC2=' '
pC3=' '
def boardprint(x=0):
    print ('   1   2   3')
    print ('A|',pA1,'|',pA2,'|',pA3,'|')
    print ('B|',pB1,'|',pB2,'|',pB3,'|')
    print ('C|',pC1,'|',pC2,'|',pC3,'|')
def tiledeterminex(x=0):
 ask=input('which tile would you like to change to x')
 if ask=='A1':
  pA1='x'
  return pA1
 elif ask=='A2':
  pA2='x'
  return pA2
 elif ask=='A3':
  pA3='x'
  return pA3
 elif ask=='B1':
  pB1='x'
  return pB1
 elif ask=='B2':
  pB2='x'
  return pB2
 elif ask=='B3':
  pB3='x'
  return pB3
 elif ask=='C1':
  pC1='x'
  return pC1
 elif ask=='C2':
  pC2='x'
  return pC2
 elif ask=='C3':
  pC3='x'
  return pC3
def tiledetermineo(x=0):
 ask=input('which tile would you like to change to o')
 if ask=='A1':
  pA1='o'
  return pA1
 elif ask=='A2':
  pA2='o'
  return pA2
 elif ask=='A3':
  pA3='o'
  return pA3
 elif ask=='B1':
  pB1='o'
  return pB1
 elif ask=='B2':
  pB2='o'
  return pB2
 elif ask=='B3':
  pB3='o'
  return pB3
 elif ask=='C1':
  pC1='o'
  return pC1
 elif ask=='C2':
  pC2='o'
  return pC2
 elif ask=='C3':
  pC3='o'
  return pC3

for i in range (0,5):
 print ('   1   2   3')
 print ('A|',pA1,'|',pA2,'|',pA3,'|')
 print ('B|',pB1,'|',pB2,'|',pB3,'|')
 print ('C|',pC1,'|',pC2,'|',pC3,'|')
 ask=input('which tile would you like to change to x')
 if ask=='A1':
   pA1='x'
 elif ask=='A2':
   pA2='x'
 elif ask=='A3':
   pA3='x'
 elif ask=='B1':
   pB1='x'
 elif ask=='B2':
   pB2='x'
 elif ask=='B3':
   pB3='x'
 elif ask=='C1':
  pC1='x'
 elif ask=='C2':
  pC2='x'
 elif ask=='C3':
  pC3='x'
 print ('   1   2   3')
 print ('A|',pA1,'|',pA2,'|',pA3,'|')
 print ('B|',pB1,'|',pB2,'|',pB3,'|')
 print ('C|',pC1,'|',pC2,'|',pC3,'|')
 ask=input('which tile would you like to change to o')
 if ask=='A1':
  pA1='o'
 elif ask=='A2':
  pA2='o'
 elif ask=='A3':
  pA3='o'
 elif ask=='B1':
  pB1='o'
 elif ask=='B2':
  pB2='o'
 elif ask=='B3':
  pB3='o'
 elif ask=='C1':
  pC1='o'
 elif ask=='C2':
  pC2='o'
 elif ask=='C3':
  pC3='o'