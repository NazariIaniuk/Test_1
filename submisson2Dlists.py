#1
numlist=[[2,5,8],
         [3,7,4],
         [1,6,9],
         [4,2,0]]
#2
row=int(input('value of what row do you want?'))
collumn=int(input('value of what collumn do you want?'))
print(numlist[row][collumn])
#3
row=int(input('which row would you like displayed?'))
print(numlist[row])
numlist[row].append(int(input('enter a new value')))
print(numlist[row])
#4
row=int(input('value of what row do you want?'))
print(numlist[row])
collumn=int(input('which value in that row do you want?'))
print(numlist[row][collumn])
ask=input('do you want to change that value?')
if ask=='yes'or ask=='y':
    newvalue=int(input('what value do you want to change it to?'))
    numlist[row][collumn]=newvalue
    print(numlist[row])
    name1=input('what is the name of the first person?')
#7
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
#8
ppllist=[{'name':name1,'age':age1,},
         {'name':name2,'age':age2,},
         {'name':name3,'age':age3,},
         {'name':name4,'age':age4,}]
print(ppllist)
#9
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