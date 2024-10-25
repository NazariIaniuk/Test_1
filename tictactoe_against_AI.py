import random
import time
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
def boardpprint (x=0):
 print('   1   2   3')
 print ('A|',pA1,'|',pA2,'|',pA3,'|')
 print ('B|',pB1,'|',pB2,'|',pB3,'|')
 print ('C|',pC1,'|',pC2,'|',pC3,'|')
def tilechange(x=0):
 print(f'it is your move {username}!')
 print(' heres how the board looks like')
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
 elif ask=='A2' and pA1==' ':
   pA2='x'
 elif ask=='A3' and pA1==' ':
   pA3='x'
 elif ask=='B1' and pA1==' ':
   pB1='x'
 elif ask=='B2' and pA1==' ':
   pB2='x'
 elif ask=='B3' and pA1==' ':
   pB3='x'
 elif ask=='C1' and pA1==' ':
  pC1='x'
 elif ask=='C2' and pA1==' ':
  pC2='x'
 elif ask=='C3' and pA1==' ':
  pC3='x'
 else:
   print('to move you need to input a value with an uppercase letter and a number like this---> B3, oh and you cant change a tile that is already taken, thats cheating! its okay you can try again in 10 seconds')
   time.sleep(10)
   a=tilechange()
def AItilechange(x=0):
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
 print (AIname,'is changing the board...')
 time.sleep(2)

while True:
 print(f'''                                                   Welcome Challanger
      this is a game of tic tac toe against the most feared Ai on the planet!, it's name is {AIname} to defeat it use a notation simiiar to chess to describe your moves
            B2 is for the center A1 and C3 are opposite corners, the board will help you not get confused in how this works!''')
 username=('what is your name challanger?')
 menu=int(input('''This is the main menu choose an option by typing a number
        1 Start game
        2 Score and statistics
        3 exit program'''))
 if menu==3:
   break
 elif menu==2:
   print(''' here are Statistics
         amount of games played:
         amount of games won :
         amount of ''')