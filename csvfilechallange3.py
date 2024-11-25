import csv
ask=int(input('how many files do you want to add?'))
for i in range(0,ask):
    books=open("books.csv", "a")
    book=input('Enter name of the book:  ')   
    Author=input('Enter the name of the authror:   ')
    year=input('Enter the release date of the book:  ')
    bookinfo='\n'+book+','+Author+','+year
    books.write(str(bookinfo))