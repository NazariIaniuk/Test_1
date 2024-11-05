numlist={0:[2,5,8],
         1:[3,7,4],
         2:[1,6,9],
         3:[4,2,0]}
row=int(input('which row would you like displayed?'))
print(numlist[row])
append=int(input('enter a new value'))
numlist[row].append(append)
print(numlist[row])