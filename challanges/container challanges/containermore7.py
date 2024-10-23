list=[962,145,702,487]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
ask=int(input('enter a 3 digit number'))
if ask in list:
    print(f' the index of this number in the list is {list.index(ask)}')
else:
    print('that is not in the list.')
    