Name=input('who do you want to invite')
print(Name,'has been invited')
counter=1
ask=input('do you want to invite another person? type y to agree')
while ask=='y':
 Name=input('who do you want to invite')
 print(Name,'has been invited')
 counter+=1
 ask=input('do you want to invite another person? type y to agree')
print ('you invited', counter,'people')
