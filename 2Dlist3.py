numlist=[[2,5,8],
         [3,7,4],
         [1,6,9],
         [4,2,0]]
row=int(input('which row would you like displayed?'))
print(numlist[row])
append=int(input('enter a new value'))
numlist[row].append(append)
print(numlist[row])