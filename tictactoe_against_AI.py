import random
import time
global gamesplayed
gamesplayed=0
gamen=1
gameswon=0
gamesAIwon=0
draws=0
global winstreak
winstreak=0
winconditionvar=0
exit=False
username='a'
adj=random.choice(['active','angry','unbeatable','super','crazy','critical'])
anme=random.choice(['Zane','Brody','Artemis','Riley','Terry','Bill','Megatron'])
AIname=(f'{adj}{anme}')
game=1
pA1=' '
pA2=' '
pA3=' '
pB1=' '
pB2=' '
pB3=' '
pC1=' '
pC2=' '
pC3=' '
def wincheck (x=0):
 global winconditionvar
 global gamesAIwon
 global gameswon
 global winstreak
 a=wincondition()
 if winconditionvar==1:
  print('You win')
  winstreak+=1
  gameswon+=1
  winconditionvar=0
 elif winconditionvar==2:
  print(f'{AIname} wins')
  winstreak=0
  gamesAIwon+=1
  winconditionvar=0
def wincondition(x=0):
 global winconditionvar
 if pA1=='x'and pA2=='x'and pA3=='x'or pB1=='x'and pB2=='x'and pB3=='x'or pC1=='x'and pC2=='x'and pC3=='x'or pA1=='x' and pB1=='x' and pC1=='x' or pA2=='x' and pB2=='x' and pC3=='x' or pA3=='x' and pB3=='x' and pC3=='x' or pA1=='x' and pB2=='x' and pC3=='x' or pA3=='x' and pB2=='x' and pC1=='x':
  winconditionvar='1'
 elif pA1=='o'and pA2=='o'and pA3=='o'or pB1=='o'and pB2=='o'and pB3=='o'or pC1=='o'and pC2=='o'and pC3=='o'or pA1=='o' and pB1=='o' and pC1=='o' or pA2=='o' and pB2=='o' and pC3=='o' or pA3=='o' and pB3=='o' and pC3=='o' or pA1=='o' and pB2=='o' and pC3=='o' or pA3=='o' and pB2=='o' and pC1=='o':
  winconditionvar='2'
def boardpprint (x=0):
 print('   1   2   3')
 print ('A|',pA1,'|',pA2,'|',pA3,'|')
 print ('B|',pB1,'|',pB2,'|',pB3,'|')
 print ('C|',pC1,'|',pC2,'|',pC3,'|')
def tilechange(x=0):
 if winconditionvar==0:
  print(f'it is your move {username}!')
  print('this is  how the board looks like')
  a=boardpprint()
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
  if ask=='A1' and pA1==' ':
    pA1='x'
  elif ask=='A2' and pA2==' ':
    pA2='x'
  elif ask=='A3' and pA3==' ':
    pA3='x'
  elif ask=='B1' and pB1==' ':
    pB1='x'
  elif ask=='B2' and pB2==' ':
    pB2='x'
  elif ask=='B3' and pB3==' ':
    pB3='x'
  elif ask=='C1' and pC1==' ':
    pC1='x'
  elif ask=='C2' and pC2==' ':
    pC2='x'
  elif ask=='C3' and pC3==' ':
    pC3='x'
  else:
    print('to move you need to input a value with an uppercase letter and a number like this---> B3, oh and you cant change a tile that is already taken, thats cheating! its okay you can try again in 10 seconds')
    time.sleep(10)
    a=tilechange()
  a=wincondition()
  return wincondition()
 else:
  return 0 
def AItilechange(x=0):
 if winconditionvar==0:
  ask=random.randint(0,9)
  global pA1
  global pA2
  global pA3
  global pB1 
  global pB2
  global pB3
  global pC1
  global pC2
  global pC3
  if ask==1 and pA1==' ':
    pA1='o'
  elif ask==2 and pA2==' ':
    pA2='o'
  elif ask==3 and pA3==' ':
    pA3='o'
  elif ask==4 and pB1==' ':
    pB1='o'
  elif ask==5 and pB2==' ':
    pB2='o'
  elif ask==6 and pB3==' ':
    pB3='o'
  elif ask==7 and pC1==' ':
    pC1='o'
  elif ask==8 and pC2==' ':
    pC2='o'
  elif ask==9 and pC3==' ':
    pC3='o'
  else:
    run=AItilechange()
  a=wincondition()
  return wincondition()
 else:
  return 0
def gameplayermove(x=0):
  global winstreak
  global draws
  global gamesplayed
  gamesplayed+=1
  print(f'this is game number {gamesplayed}')
  a=tilechange()
  if a==0:
    a=wincheck()
  a=AItilechange()
  a=tilechange()
  a=AItilechange()
  a=tilechange()
  a=AItilechange()
  a=tilechange()
  a=AItilechange()
  a=tilechange()
  print('this is a draw!')
  draws+=1
  winstreak=0
def gameAImove(x=0):
 global winstreak
 global gamesplayed
 gamesplayed+=1
 print(f'this is game {gamesplayed}, AI moves first this time')
 a=AItilechange()
 a=tilechange()
 a=AItilechange()
 a=tilechange()
 a=AItilechange()
 a=tilechange()
 a=AItilechange()
 a=tilechange()
 a=AItilechange()
 print('this is a draw')
 draws+=1
 winstreak=0
while True:
 print(f'''                                                   Welcome Challanger
      this is a game of tic tac toe against the most feared Ai on the planet!, it's name is {AIname} to defeat it use a notation simiiar to chess to describe your moves
            B2 is for the center A1 and C3 are opposite corners, the board will help you not get confused in how this works!''')
 username=input('what is your name challanger?')
 print(f'welcome {username}')
 
 menu=int(input('''This is the main menu, choose an option by typing a number
        1 Start game
        2 Score and statistics
        3 exit program'''))
 if menu==3:
   break
 elif menu==2:
   print(f''' here are Statistics!
         amount of games played:  {gamesplayed}
         amount of games won :    {gameswon}
         amount of games AI won:  {gamesAIwon}
         amount of draws:         {draws}                  
         current winstreak :      {winstreak}      
         AI name :                {AIname}
         player name:             {username}''')
 elif menu==1:
   while True:
    if gamen/2!=gamen//2:
     a=gameplayermove()
    else:
     a=gameAImove()
      