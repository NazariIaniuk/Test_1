namefile=open('Names.txt', 'r')
namelist=namefile.read()
namelist=namelist.split('\n')
print(namelist)
namelist.remove(input('enter a name that is on the list'))
namefile2=open('Names2','w')
for i in namelist:
    namefile2.write(i+'\n')