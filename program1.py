dictionary={'Freddie mercury':'Killer Qeen', 
             'Michael jackson' :'Billie Jean',
             'Elvis presley':'All Shook Up'}
name=input('name a singer').capitalize()
if name in dictionary:
    print(dictionary[name])
else:
    print('not in dictionary')
    ask2=input('would you liek to add the name to the dictionary?')
    if ask2=='yes' or ask2=='y':
        song=input('input a song written by that artist')
        dictionary[name]=song
        
