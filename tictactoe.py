
p11=' '
p12=' '
p13=' '
p21=' '
p22=' '
p23=' '
p31=' '
p32=' '
p33=' '
def boardprint(x=0):
    print ('  1   2   3')
    print ('|',p11,'|',p12,'|',p13,'|')
    print ('|',p21,'|',p22,'|',p23,'|')
    print ('|',p31,'|',p32,'|',p33,'|')
    return 0 
def tiledetermine(x=0):
    ask=int(input('which tile would you like to move in?'))
    if ask==11:
     p11='x'
printboard=boardprint()
