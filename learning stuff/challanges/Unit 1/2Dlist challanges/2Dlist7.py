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
ppllist=[{'age':age1,'shoesize':shoesize1},
         {'age':age2,'shoesize':shoesize2},
         {'age':age3,'shoesize':shoesize3},
         {'age':age4,'shoesize':shoesize4}]
ask=input('data for who do you want to see?')
if ask==name1:
    print (ppllist[1])
if ask==name2:
    print (ppllist[3])   
if ask==name3:
    print (ppllist[5])
if ask==name4:
    print (ppllist[7])
