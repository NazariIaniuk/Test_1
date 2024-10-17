list=['red','orange','yellow']
print(list[0])
print(list[1])
print(list[2])
ask=input('name another color')
postion=int(input('which postion in the list do you want it to take'))
postion-=1
list.insert(postion, ask)
print(list)
delete=input('which color would you like to remove')
list.remove(delete)
print(list)