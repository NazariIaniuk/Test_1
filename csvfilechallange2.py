import csv
books=open("books.csv", "a")
book=input('Enter name of the book:  ')   
Author=input('Enter the name of the authror:   ')
year=input('Enter the release date of the book:  ')
bookinfo='\n'+book+','+Author+','+year
books.write(str(bookinfo))
books=open("books.csv","r")
for row in books:
 print(row)


books=open("books.csv","r")
reader=csv.reader(books)
rowlist=list(reader)
print(rowlist)