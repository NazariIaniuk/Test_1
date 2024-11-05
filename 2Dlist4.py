numlist={0:[2,5,8],
         1:[3,7,4],
         2:[1,6,9],
         3:[4,2,0]}
row=int(input('value of what row do you want?'))
print(numlist[row])
collumn=int(input('which value in that row do you want?'))
print(numlist[row][collumn])
ask=input('do you want to change that value?')
if ask=='yes'or ask=='y':
    newvalue=int(input('what value do you want to change it to?'))
    numlist[row][collumn]=newvalue
    print(numlist[row])