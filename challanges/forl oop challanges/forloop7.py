ask=int(input('how much people do you want to invite to the party'))
if ask>10: 
 print('too many people')
elif ask<=10:
    for i in range (0,ask):
     name=input('what is their name?')
     print(name,'has been invited')