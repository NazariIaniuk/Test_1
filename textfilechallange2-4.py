namefile= open('Names.txt', 'r')
print(namefile.read())
namefile= open('Names.txt', 'a')
namefile.write('\n')
namefile.write(input('enter a new name'))
namefile= open('Names.txt', 'r')
print(namefile.read())