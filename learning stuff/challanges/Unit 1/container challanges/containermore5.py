ask1=input('what is a food you like?')
ask2=input('what is another food you like?')
ask3=input('what is another food you like?')
ask4=input('what is another food you like?')
list=[ask1,'1',ask2,'2',ask3,'3',ask4,'4']
a=int(input('type the index of the food you will remove'))
print(list)
a*=2
a-=2
list.remove(list[a])
list.sort
print(list)