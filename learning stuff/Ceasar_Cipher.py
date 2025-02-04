numberedmessage=list()
encryptedmessage=str()
msgstring=str()
def encrypt (x=0):
    global encryptedmessage
    message=input('enter the message you need to encrypt:')
    shiftvalue=int(input('enter the shift value:'))
    while shiftvalue>=51:
     shiftvalue-=50
    while shiftvalue<0:
     shiftvalue+=50
    for letter in message:
        if letter=='a':
           numberedmessage.append(1+shiftvalue)
        elif letter=='b':
           numberedmessage.append(2+shiftvalue)
        elif letter=='c':
           numberedmessage.append(3+shiftvalue)
        elif letter=='d':
           numberedmessage.append(4+shiftvalue)
        elif letter=='e':
           numberedmessage.append(5+shiftvalue)
        elif letter=='f':
           numberedmessage.append(6+shiftvalue)
        elif letter=='g':
           numberedmessage.append(7+shiftvalue)
        elif letter=='h':
           numberedmessage.append(8+shiftvalue)
        elif letter=='i':
           numberedmessage.append(9+shiftvalue)
        elif letter=='j':
           numberedmessage.append(10+shiftvalue)
        elif letter=='k':
           numberedmessage.append(11+shiftvalue)
        elif letter=='l':
           numberedmessage.append(12+shiftvalue)
        elif letter=='m':
           numberedmessage.append(13+shiftvalue)
        elif letter=='n':
           numberedmessage.append(14+shiftvalue)
        elif letter=='o':
           numberedmessage.append(15+shiftvalue)
        elif letter=='p':
           numberedmessage.append(16+shiftvalue)
        elif letter=='q':
           numberedmessage.append(17+shiftvalue)
        elif letter=='r':
           numberedmessage.append(18+shiftvalue)
        elif letter=='s':
           numberedmessage.append(19+shiftvalue)
        elif letter=='t':
           numberedmessage.append(20+shiftvalue)
        elif letter=='u':
           numberedmessage.append(21+shiftvalue)
        elif letter=='v':
           numberedmessage.append(22+shiftvalue)
        elif letter=='w':
           numberedmessage.append(23+shiftvalue)
        elif letter=='x':
           numberedmessage.append(24+shiftvalue)
        elif letter=='y':
           numberedmessage.append(25+shiftvalue)
        elif letter=='z':
           numberedmessage.append(26+shiftvalue)
        elif letter==' ':
           numberedmessage.append(27+shiftvalue)
        elif letter==',':
           numberedmessage.append(28+shiftvalue)
        elif letter=='.':
           numberedmessage.append(29+shiftvalue)
        elif letter=='!':
           numberedmessage.append(30+shiftvalue)
        elif letter=='?':
           numberedmessage.append(31+shiftvalue)
        elif letter=='@':
           numberedmessage.append(32+shiftvalue)
        elif letter=='1':
           numberedmessage.append(33+shiftvalue)
        elif letter=='2':
           numberedmessage.append(34+shiftvalue)
        elif letter=='3':
           numberedmessage.append(35+shiftvalue)
        elif letter=='4':
           numberedmessage.append(36+shiftvalue)
        elif letter=='5':
           numberedmessage.append(37+shiftvalue)
        elif letter=='6':
           numberedmessage.append(38+shiftvalue)
        elif letter=='7':
           numberedmessage.append(39+shiftvalue)
        elif letter=='8':
           numberedmessage.append(40+shiftvalue)
        elif letter=='9':
           numberedmessage.append(41+shiftvalue)
        elif letter=='0':
           numberedmessage.append(42+shiftvalue)
        elif letter=='(':
           numberedmessage.append(43+shiftvalue)
        elif letter==')':
           numberedmessage.append(44+shiftvalue)
        elif letter==':':
           numberedmessage.append(45+shiftvalue)
        elif letter=='/':
           numberedmessage.append(46+shiftvalue)
        elif letter=='\n':
           numberedmessage.append(47+shiftvalue)
        elif letter==';':
           numberedmessage.append(48+shiftvalue)
        elif letter=='=':
           numberedmessage.append(49+shiftvalue)
        elif letter=='+':
           numberedmessage.append(50+shiftvalue)
    for i in numberedmessage:
        if i<0:
         i+=50
        if i>=51:
         i-=50
    for i in numberedmessage:
        if i==1:
           encryptedmessage+=('a')
        elif i==2:
           encryptedmessage+=('b')
        elif i==3:
           encryptedmessage+=('c')
        elif i==4:
           encryptedmessage+=('d')
        elif i==5:
           encryptedmessage+=('e')
        elif i==6:
           encryptedmessage+=('f')
        elif i==7:
           encryptedmessage+=('g')
        elif i==8:
           encryptedmessage+=('h')
        elif i==9:
           encryptedmessage+=('i')
        elif i==10:
           encryptedmessage+=('j')
        elif i==11:
           encryptedmessage+=('k')
        elif i==12:
           encryptedmessage+=('l')
        elif i==13:
           encryptedmessage+=('m')
        elif i==14:
           encryptedmessage+=('n')
        elif i==15:
           encryptedmessage+=('o')
        elif i==16:
           encryptedmessage+=('p')
        elif i==17:
           encryptedmessage+=('q')
        elif i==18:
           encryptedmessage+=('r')
        elif i==19:
           encryptedmessage+=('s')
        elif i==20:
           encryptedmessage+=('t')
        elif i==21:
           encryptedmessage+=('u')
        elif i==22:
           encryptedmessage+=('v')
        elif i==23:
           encryptedmessage+=('w')
        elif i==24:
           encryptedmessage+=('x')
        elif i==25:
           encryptedmessage+=('y')
        elif i==26:
           encryptedmessage+=('z')
        elif i==27:
           encryptedmessage+=(' ')
        elif i==28:
           encryptedmessage+=(',')
        elif i==29:
           encryptedmessage+=('.')
        elif i==30:
           encryptedmessage+=('!')
        elif i==31:
           encryptedmessage+=('?')
        elif i==32:
           encryptedmessage+=('@')
        elif i==33:
           encryptedmessage+=('1')
        elif i==34:
           encryptedmessage+=('2')
        elif i==35:
           encryptedmessage+=('3')
        elif i==36:
           encryptedmessage+=('4')
        elif i==37:
           encryptedmessage+=('5')
        elif i==38:
           encryptedmessage+=('6')
        elif i==39:
           encryptedmessage+=('7')
        elif i==40:
           encryptedmessage+=('8')
        elif i==41:
           encryptedmessage+=('9')
        elif i==42:
           encryptedmessage+=('0')
        elif i==43:
           encryptedmessage+=('(')
        elif i==44:
           encryptedmessage+=(')')
        elif i==45:
           encryptedmessage+=(':')
        elif i==46:
           encryptedmessage+=('/')
        elif i==47:
           encryptedmessage+=('\n')
        elif i==48:
           encryptedmessage+=(';')
        elif i==49:
           encryptedmessage+=('=')
        elif i==50:
           encryptedmessage+=('+')
    print('here is the encrypted message',encryptedmessage)
def decrypt (x=0):
    global encryptedmessage
    message=input('enter the message you need to decrypt:')
    shiftvalue=int(input('enter the shift value that was used to encrypt the message:'))
    while shiftvalue>=51:
     shiftvalue-=50
    while shiftvalue<0:
     shiftvalue+=50
    shiftvalue-=shiftvalue*2
    shiftvalue+=50
    for letter in message:
        if letter=='a':
           numberedmessage.append(1+shiftvalue)
        elif letter=='b':
           numberedmessage.append(2+shiftvalue)
        elif letter=='c':
           numberedmessage.append(3+shiftvalue)
        elif letter=='d':
           numberedmessage.append(4+shiftvalue)
        elif letter=='e':
           numberedmessage.append(5+shiftvalue)
        elif letter=='f':
           numberedmessage.append(6+shiftvalue)
        elif letter=='g':
           numberedmessage.append(7+shiftvalue)
        elif letter=='h':
           numberedmessage.append(8+shiftvalue)
        elif letter=='i':
           numberedmessage.append(9+shiftvalue)
        elif letter=='j':
           numberedmessage.append(10+shiftvalue)
        elif letter=='k':
           numberedmessage.append(11+shiftvalue)
        elif letter=='l':
           numberedmessage.append(12+shiftvalue)
        elif letter=='m':
           numberedmessage.append(13+shiftvalue)
        elif letter=='n':
           numberedmessage.append(14+shiftvalue)
        elif letter=='o':
           numberedmessage.append(15+shiftvalue)
        elif letter=='p':
           numberedmessage.append(16+shiftvalue)
        elif letter=='q':
           numberedmessage.append(17+shiftvalue)
        elif letter=='r':
           numberedmessage.append(18+shiftvalue)
        elif letter=='s':
           numberedmessage.append(19+shiftvalue)
        elif letter=='t':
           numberedmessage.append(20+shiftvalue)
        elif letter=='u':
           numberedmessage.append(21+shiftvalue)
        elif letter=='v':
           numberedmessage.append(22+shiftvalue)
        elif letter=='w':
           numberedmessage.append(23+shiftvalue)
        elif letter=='x':
           numberedmessage.append(24+shiftvalue)
        elif letter=='y':
           numberedmessage.append(25+shiftvalue)
        elif letter=='z':
           numberedmessage.append(26+shiftvalue)
        elif letter==' ':
           numberedmessage.append(27+shiftvalue)
        elif letter==',':
           numberedmessage.append(28+shiftvalue)
        elif letter=='.':
           numberedmessage.append(29+shiftvalue)
        elif letter=='!':
           numberedmessage.append(30+shiftvalue)
        elif letter=='?':
           numberedmessage.append(31+shiftvalue)
        elif letter=='@':
           numberedmessage.append(32+shiftvalue)
        elif letter=='1':
           numberedmessage.append(33+shiftvalue)
        elif letter=='2':
           numberedmessage.append(34+shiftvalue)
        elif letter=='3':
           numberedmessage.append(35+shiftvalue)
        elif letter=='4':
           numberedmessage.append(36+shiftvalue)
        elif letter=='5':
           numberedmessage.append(37+shiftvalue)
        elif letter=='6':
           numberedmessage.append(38+shiftvalue)
        elif letter=='7':
           numberedmessage.append(39+shiftvalue)
        elif letter=='8':
           numberedmessage.append(40+shiftvalue)
        elif letter=='9':
           numberedmessage.append(41+shiftvalue)
        elif letter=='0':
           numberedmessage.append(42+shiftvalue)
        elif letter=='(':
           numberedmessage.append(43+shiftvalue)
        elif letter==')':
           numberedmessage.append(44+shiftvalue)
        elif letter==':':
           numberedmessage.append(45+shiftvalue)
        elif letter=='/':
           numberedmessage.append(46+shiftvalue)
        elif letter=='\n':
           numberedmessage.append(47+shiftvalue)
        elif letter==';':
           numberedmessage.append(48+shiftvalue)
        elif letter=='=':
           numberedmessage.append(49+shiftvalue)
        elif letter=='+':
           numberedmessage.append(50+shiftvalue)
    for i in numberedmessage:
        if i<0:
         i+=50
        if i>=51:
         i-=50
    for i in numberedmessage:
        if i==1:
           encryptedmessage+=('a')
        elif i==2:
           encryptedmessage+=('b')
        elif i==3:
           encryptedmessage+=('c')
        elif i==4:
           encryptedmessage+=('d')
        elif i==5:
           encryptedmessage+=('e')
        elif i==6:
           encryptedmessage+=('f')
        elif i==7:
           encryptedmessage+=('g')
        elif i==8:
           encryptedmessage+=('h')
        elif i==9:
           encryptedmessage+=('i')
        elif i==10:
           encryptedmessage+=('j')
        elif i==11:
           encryptedmessage+=('k')
        elif i==12:
           encryptedmessage+=('l')
        elif i==13:
           encryptedmessage+=('m')
        elif i==14:
           encryptedmessage+=('n')
        elif i==15:
           encryptedmessage+=('o')
        elif i==16:
           encryptedmessage+=('p')
        elif i==17:
           encryptedmessage+=('q')
        elif i==18:
           encryptedmessage+=('r')
        elif i==19:
           encryptedmessage+=('s')
        elif i==20:
           encryptedmessage+=('t')
        elif i==21:
           encryptedmessage+=('u')
        elif i==22:
           encryptedmessage+=('v')
        elif i==23:
           encryptedmessage+=('w')
        elif i==24:
           encryptedmessage+=('x')
        elif i==25:
           encryptedmessage+=('y')
        elif i==26:
           encryptedmessage+=('z')
        elif i==27:
           encryptedmessage+=(' ')
        elif i==28:
           encryptedmessage+=(',')
        elif i==29:
           encryptedmessage+=('.')
        elif i==30:
           encryptedmessage+=('!')
        elif i==31:
           encryptedmessage+=('?')
        elif i==32:
           encryptedmessage+=('@')
        elif i==33:
           encryptedmessage+=('1')
        elif i==34:
           encryptedmessage+=('2')
        elif i==35:
           encryptedmessage+=('3')
        elif i==36:
           encryptedmessage+=('4')
        elif i==37:
           encryptedmessage+=('5')
        elif i==38:
           encryptedmessage+=('6')
        elif i==39:
           encryptedmessage+=('7')
        elif i==40:
           encryptedmessage+=('8')
        elif i==41:
           encryptedmessage+=('9')
        elif i==42:
           encryptedmessage+=('0')
        elif i==43:
           encryptedmessage+=('(')
        elif i==44:
           encryptedmessage+=(')')
        elif i==45:
           encryptedmessage+=(':')
        elif i==46:
           encryptedmessage+=('/')
        elif i==47:
           encryptedmessage+=('\n')
        elif i==48:
           encryptedmessage+=(';')
        elif i==49:
           encryptedmessage+=('=')
        elif i==50:
           encryptedmessage+=('+')
    print (encryptedmessage)
while True:
 menu=int(input('''       MENU
 1) encypt message
 2) decrypt message
 3) exit                '''))
 if menu==1:
    run=encrypt()
 elif menu==2:
    run=decrypt()
 elif menu==3:
    break