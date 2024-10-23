ask='yyy'
partylist=list()
invite=input('enter a name of a person you would like to invite')
partylist.append(invite)
invite=input('enter a name of another person you would like to invite')
partylist.append(invite)
invite=input('and another one')
partylist.append(invite)
while ask !='no':
 ask=input('do you want to add another one?')
 if ask=='yes' or ask=='y':
  invite=input('who would you like to invite')
  partylist.append(invite)
print(len(partylist))