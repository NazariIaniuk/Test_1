import csv
for i in range(int(input('enter the starting year')),int(input('enter the end year'))+1):
    books=open ('books.csv', 'r')
    reader=csv.reader(books)
    for row in books:
     if str(i) in row:
        print (row)