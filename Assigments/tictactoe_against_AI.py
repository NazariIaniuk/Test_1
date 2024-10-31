#imports and starting values for variables
import random
import time
ask='y'
newround=False
stopgame=False
gamesplayed=0
gameswon=0
gamesAIwon=0
draws=0
winstreak=0
winconditionvar=0
exit=False
username='a'
adj=random.choice(['Active','Angry','Unbeatable','Super','Crazy','Critical'])
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
# definintions if one of them seems useless, trust me it isnt
def AItilechangerepeat(x=0):
 time.sleep(0.3)
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
    run=AItilechangerepeat()
  a=wincondition()
  return wincondition()
 else:
  return 0
def boardreset(x=0):
  global pA1
  global pA2
  global pA3
  global pB1
  global pB2
  global pB3
  global pC1
  global pC2
  global pC3
  pA1=' '
  pA2=' '
  pA3=' '
  pB1=' '
  pB2=' '
  pB3=' '
  pC1=' '
  pC2=' '
  pC3=' '
def wincheck(x=0):
 global winconditionvar
 global gamesAIwon
 global ask
 global stopgame
 global newround
 global gameswon
 global winstreak
 a=wincondition()
 if winconditionvar==1:
  print('You win')
  time.sleep(1)
  winstreak+=1
  print(f'Your winstreak is now {winstreak}')
  gameswon+=1
  winconditionvar=0
  a=boardreset()
  ask=input('do you want to play another round?')
  if ask=='y'or ask=='yes':
    newround=True
  elif ask=='n'or ask=='no' or ask=='NO':
    stopgame=True
 elif winconditionvar==2:
  print(f'{AIname} wins')
  winstreak=0
  gamesAIwon+=1
  winconditionvar=0
  a=boardreset()
  ask=input('do you want to play another round?')
  if ask=='y'or ask=='yes':
    newround=True
  elif ask=='n'or ask=='no' or ask=='NO':
    stopgame=True
def wincondition(x=0):
 global winconditionvar
 if pA1=='x'and pA2=='x'and pA3=='x'or pB1=='x'and pB2=='x'and pB3=='x'or pC1=='x'and pC2=='x'and pC3=='x'or pA1=='x' and pB1=='x' and pC1=='x' or pA2=='x' and pB2=='x' and pC2=='x' or pA3=='x' and pB3=='x' and pC3=='x' or pA1=='x' and pB2=='x' and pC3=='x' or pA3=='x' and pB2=='x' and pC1=='x':
  winconditionvar=1
 elif pA1=='o'and pA2=='o'and pA3=='o'or pB1=='o'and pB2=='o'and pB3=='o'or pC1=='o'and pC2=='o'and pC3=='o'or pA1=='o' and pB1=='o' and pC1=='o' or pA2=='o' and pB2=='o' and pC2=='o' or pA3=='o' and pB3=='o' and pC3=='o' or pA1=='o' and pB2=='o' and pC3=='o' or pA3=='o' and pB2=='o' and pC1=='o':
  winconditionvar=2
def boardpprint(x=0):
 print('   1   2   3')
 print ('A|',pA1,'|',pA2,'|',pA3,'|')
 print ('B|',pB1,'|',pB2,'|',pB3,'|')
 print ('C|',pC1,'|',pC2,'|',pC3,'|')
def tilechange(x=0):
 if stopgame==True:
  return 3
 if newround==True:
  run=gameAImove()
 if winconditionvar!=0:
  run=wincheck()
 else:
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
def AItilechange(x=0):
 if stopgame==True:
  return 3
 if newround==True:
  run=gameplayermove()
 if winconditionvar!=0:
  run=wincheck()
 else:
  print(f'{AIname} is thinking')
  time.sleep(1)
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
    run=AItilechangerepeat()
  a=wincondition()
  return wincondition()
def gameplayermove(x=0):
  global newround
  newround=False
  global winstreak
  global draws
  global winconditionvar
  global gamesplayed
  gamesplayed+=1
  print(f'this is game number {gamesplayed}')
  time.sleep(1)
  a=tilechange()
  a=AItilechange()
  a=tilechange()
  a=AItilechange()
  a=tilechange()
  a=AItilechange()
  a=tilechange()
  a=AItilechange()
  a=tilechange()
  a=wincondition()
  a=wincheck()
  if newround==True:
   run=gameAImove()
  if stopgame==False:
   print('this is a draw!')
   draws+=1
   winstreak=0
   winconditionvar=0
   a=boardreset()
def gameAImove(x=0):
  global newround
  newround=False
  global winstreak
  global winconditionvar
  global gamesplayed
  global draws
  gamesplayed+=1
  print(f'this is game {gamesplayed}, AI moves first')
  time.sleep(1)
  a=AItilechange()
  a=tilechange()
  a=AItilechange()
  a=tilechange()
  a=AItilechange()
  a=tilechange()
  a=AItilechange()
  a=tilechange()
  a=AItilechange()
  run=wincheck()
  if newround==True:
    run=gameplayermove()
  if stopgame==False:
   print('this is a draw')
   draws+=1
   winstreak=0
   winconditionvar=0
   a=boardreset()
  else:
    return 0
#single use commands as well as a while loop for the menu
print(f'''                                                   Welcome Challanger
     this is a game of tic tac toe against the most feared Ai on the planet!, it's name is {AIname} to defeat it use a notation simiiar to chess to describe your moves
            B2 is for the center A1 and C3 are opposite corners, the board will help you not get confused in how this works!''')
username=input('what is your name challanger?')
print(f'         welcome {username}!')
time.sleep(1)
while True:
 menu=int(input(''' This is the main menu, choose an option by typing a number
        1 Start game
        2 Score and statistics
        3 exit program'''))
 if menu==3:
   break
 elif menu==2:
  time.sleep(1)
  print(f'''                    Here are Statistics!
        ___________________________________________________
        | amount of games played:   {gamesplayed}
        | amount of games won :     {gameswon}
        | amount of games AI won:   {gamesAIwon}
        | amount of draws:          {draws}                 
        | current winstreak :       {winstreak}      
        | AI name :                 {AIname}
        | player name:              {username}''')
  time.sleep(4)
 elif menu==1:
   stopgame=False
   newround=False
   integer=random.randint(1,2)
   if integer==1:
    run=gameplayermove()
   elif integer==2:
    run=gameAImove()
# game features: 1 no bugs that can get an advantage to the player, possibity for both the player and AI to move first, comprehensive UI and a display of the board, the game scans the board to see if the AI or the player won the game by checking the values of tiles
# if you find any bugs that would mean i didn't see them during testing