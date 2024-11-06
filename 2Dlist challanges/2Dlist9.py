name1=input('what is the name of the first person?')
age1=int(input('what is their age?'))
shoesize1=int(input('what is their shoe size?'))
name2=input('what is the name of the Second person?')
age2=int(input('what is their age?'))
shoesize2=int(input('what is their shoe size?'))
name3=input('what is the name of the Third person?')
age3=int(input('what is their age?'))
shoesize3=int(input('what is their shoe size?'))
name4=input('what is the name of the Fourth person?')
age4=int(input('what is their age?'))
shoesize4=int(input('what is their shoe size?'))
ppllist=[{'name':name1,'age':age1,'shoesize':shoesize1},
         {'name':name2,'age':age2,'shoesize':shoesize2},
         {'name':name3,'age':age3,'shoesize':shoesize3},
         {'name':name4,'age':age4,'shoesize':shoesize4}]
ask=input('data for who do you want to remove')
if ask==name1:
 ppllist.remove({'name':name1,'age':age1,'shoesize':shoesize1})
if ask==name2:
 ppllist.remove({'name':name2,'age':age2,'shoesize':shoesize2}) 
if ask==name3:
 ppllist.remove({'name':name3,'age':age3,'shoesize':shoesize3})
if ask==name4:
 ppllist.remove({'name':name4,'age':age4,'shoesize':shoesize4})
for i in range (0,3):
 print(ppllist[i])