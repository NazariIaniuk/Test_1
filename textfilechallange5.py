while True:
    menu=int(input('''select an action by inputting a number 
    1) create new file
    2) Display the file
    3) Add a new item to the file.'''))
    if menu>=3 or menu <=1:
        print('choose an option on the menu please')
    if menu==1:
        ask=