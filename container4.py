dictionary={'height':'143cm', 'Favorite color':'green','favorite actor':'THE ROCK'}
ask=int(input('''ask about height color or Favorite actor
              1 height
              2 favorite color
              3 favorite actor'''))
if ask==1:
    print(dictionary['height'])
elif ask==2:
    print(dictionary['Favorite color'])
elif ask==3:
    print(dictionary['favorite actor'])