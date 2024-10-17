namelist=list()
for i in range(0,5):
 name=input('enter a name')
 namelist.append(name)
print(namelist)
delnum=int(input('enter a number from 1 to 5 to delete a certain name'))
delnum-=1
namelist.pop(delnum)
print(namelist)