namefile=open('Names.txt', 'r')
Namefile2=open('Names2.txt','w')
print(namefile.read())
find=input('enter a name  that is in the list ')
for row in 'Names.txt' :
    if find in 'Names.txt':
     print('deleted')
    else:
        Namefile2=open('Names2.txt','')
        Namefile2.write(row)
Namefile2=open('Names2.txt','r')
print(Namefile2.read)



