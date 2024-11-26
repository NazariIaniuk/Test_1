namefile=open('Names.txt', 'r')
Namefile2=open('Names2.txt','w')
print(namefile.read())
find=input('enter a name  that is in the list ')
for row in namefile.read():
    print(row)