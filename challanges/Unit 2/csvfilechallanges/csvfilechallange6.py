import csv
booklist=list(csv.reader(open('books.csv', 'r')))
print(booklist)
del booklist[int(input('which row do you want to delete?'))-1]
print(booklist)
row=int(input('which row would you like to edit?'))-1
booklist[row]=[input('enter new book name'),input('enter new author name'),int(input('enter new year of release'))]
print(booklist)
books=open('books.csv','w')
for row in booklist:
  books.write(row[0]+','+row[1]+','+str(row[2])+'\n')


# if you need the original info from the books.csv

#To kill a mockingbird,Harper lee,1960
#A brief history of time,Stephen Hawking,1988
#The great Gatsby,F.Scott fitzgerald,1922
#The Man Who Mistook His Wife for a Hat,Oliver Sacks,1985
#Pride and Prejudice,Jane Auste,1813