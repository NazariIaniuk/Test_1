import csv
booklist=list(csv.reader(open('books.csv', 'r')))
print(booklist)
del booklist[int(input('which row do you want to delete?'))-1]
print(booklist)
row=int(input('which row would you like to edit?'))-1
booklist[row]=[input('enter new book name'),input('enter new author name'),int(input('enter new year of release'))]
print(booklist)
for row in booklist:
 opener=open('books.csv','w')