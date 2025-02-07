def balancesheet(x=0):
 assetlist=[]
 valuelist=[]
 ask1='y'
 while ask1!='no':
  asset=input('name of asset:')
  number=int(input('price tied to asset'))
  assetlist.append(asset)
  valuelist.append(number)


  
  








while True: 
 accounitngwork=int(input('''which accounting work would you like to do
                          1) get balance sheet info'''))
 if accounitngwork==1:
  run=assetscalc()
