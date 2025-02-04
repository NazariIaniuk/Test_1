shopping_cart=list()
while True:
 menu=int(input('''what action would you like to do?
               1) add item to shopping cart
               2) see shopping cart list
               3) remove item from shopping cart
               4) edit an item inside shopping cart
               5) remove all items from shopping cart
               6) exit'''))
 if menu==1:
  ask=input('what would you like to add?')
  shopping_cart.append(ask)
 elif menu==2:
  print(shopping_cart)
 elif menu==3:
  ask=int(input('what is the index of the item you would like to remove?'))
  del shopping_cart[ask]
 elif menu==4:
  num=int(input('what is the index of the item you want to edit?'))
  ask=input(f'the item you chose is {shopping_cart[num]} what would you like to change it to? ')
  shopping_cart[num]=ask
 elif menu==5:
  del shopping_cart[0:len(shopping_cart)]
 elif menu==6:
  break