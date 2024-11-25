import csv
for i in range(0,int(input('how many files do you want to add?'))):
    books=open('books.csv', 'a')
    book=input('Enter name of the book:  ')   
    Author=input('Enter the name of the authror:   ')
    year=input('Enter the release date of the book:  ')
    bookinfo='\n'+book+','+Author+','+year
    books.write(str(bookinfo))
books=open ('books.csv', 'r')
reader=csv.reader(books)
searchrequest=input('enter the name of the author you want to find:  ')
for row in books:
    if searchrequest in str(row):
        print (row)