def balancesheet(x=0):
 ask1=int(input('''what do you have availiable to you?
                1 assets and equity
                2 liabilities and equity
                3 assets and liabilities
                4 all information'''))
def assetscalc(x=0):
 dictionarylist=[]
 sortinglist=[]
 ask1='y'
 while ask1!='no':
  asset=input('name of asset:')
  number=int(input('price tied to asset'))
  dictionary={number:asset}
  sortinglist.append(number)
  dictionarylist.append(dictionary)
  ask1=input('add more?')


  
  













while True: 
 accounitngwork=int(input('''which accounting work would you like to do
                          1) get balance sheet info'''))
 if accounitngwork==1:
  run=balancesheet()
