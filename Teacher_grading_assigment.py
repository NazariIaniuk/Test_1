import statistics
grades=[]
studentlist=[]
ask=int(input('how many students are there?'))
for i in range(0,ask):
 name=input('what is the name of the student?')
 value=int(input('what is the total value of the assignment?'))
 grade=int(input('what is the grade the student got?'))
 smallerlist={name:(grade/value*100)}
 studentlist.append(smallerlist)
 grades.append(grade/value*100)
 print(studentlist)
print(f'the mean of class grades,{statistics.mean(grades)}%')
print(f'the median of class grades,{statistics.median(grades)}%')
print(f'the mode of class grades,{statistics.mode(grades)}%')