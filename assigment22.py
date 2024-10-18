word=input('input any word')
list=list()
for i in word:
 list.append(i)
list.append(list[0])
list.pop(0)
list.append('ay')
print(f'{list}')