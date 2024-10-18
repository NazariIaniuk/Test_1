word=input('input any word')
list=list()
for i in word:
 list.append(i)
list.append(list[0])
list[0]=list[-2]
list.pop(-2)
print(list)