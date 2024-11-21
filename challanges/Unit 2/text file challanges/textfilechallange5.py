while True:
    menu=int(input('''select an action by inputting a number 
    1) create new file
    2) Display the file
    3) Add a new item to the file.'''))
    if menu>3 or menu <1:
        print('choose an option on the menu please')
    elif menu==1:
        subjectfile=open('Subject.txt','w')
        subjectfile.write(str(input('enter a school subject')))
    elif menu==2:
        subjectfile=open('Subject.txt','r')
        print(subjectfile.read())
    elif menu==3:
        subjectfile=open('Subject.txt','a')
        subjectfile.write('\n')
        subjectfile.write(str(input('what subject would you like to add to the list')))
        subjectfile.close
        subjectfile=open('Subject.txt','r')
        print(subjectfile.read())