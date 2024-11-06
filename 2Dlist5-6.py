geolist={'John':{'N':3056,'S':8463,'E':8441,'W':2694},
         'Tom':{'N':4832,'S':6786,'E':4737,'W':3612},
         'Anne':{'N':5239,'S':4802,'E':5820,'W':1859},
         'Fiona':{'N':3904,'S':3645,'E':8821,'W':2451}}
name=input('value of what name do you want?')
region=input('value of what region do you want?')
print(geolist[name][region])
name=input('value of what name do you want to change?')
region=input('value of what region do you want to change?')
geolist[name][region]=int(input('what do you want to change it to?'))
print(geolist[name])