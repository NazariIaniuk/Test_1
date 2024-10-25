#container 3

container3dictionary={'height':'143cm', 'Favorite color':'green','favorite actor':'THE ROCK'}
#container 4

container4dictionary={'height':'143cm', 'Favorite color':'green','favorite actor':'THE ROCK'}
ask=int(input('''ask about height color or Favorite actor
              1 height
              2 favorite color
              3 favorite actor'''))
if ask==1:
    print(container3dictionary['height'])
elif ask==2:
    print(container3dictionary['Favorite color'])
elif ask==3:
    print(container3dictionary['favorite actor'])

#containermore5
cm5ask1=input('what is a food you like?')
cm5ask2=input('what is another food you like?')
cm5ask3=input('what is another food you like?')
cm5ask4=input('what is another food you like?')
cm5list=[cm5ask1,'1',cm5ask2,'2',cm5ask3,'3',cm5ask4,'4']
a5=int(input('type the index of the food you will remove'))
print(list)
a5*=2
a5=2
list.remove(list[a5])
list.sort
print(list)
#containermore6
cm6list=['red','yellow','blue','green','orange','purple','cyan','teal','brown','white']
cm6ask1=int(input('enter a number between 0 and 4'))
cm6ask2=int(input('enter an end number between 5 and 9'))
print(cm6list[cm6ask1:cm6ask2])
#containermore8
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