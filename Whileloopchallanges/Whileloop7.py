num=10
while num>0:
 print ('there are',num,'green bottles hanging on the wall',num,'green bottles hanging on the wall, and if 1 green bottle should accidentaly fall')
 ask=int(input('how many green bottles will be hanging on the wall?'))
 ask+=1
 if ask==num:
     num-=1
 else:
     print('no,try again')
print('There are no more green bottles hanging on the wall')