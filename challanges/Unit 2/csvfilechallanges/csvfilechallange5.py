import csv
x=1
books=open ('books.csv', 'r')
reader=csv.reader(books)
for row in books:
 print (x,row)
 x+=1