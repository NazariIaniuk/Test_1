import statistics
grades=[]
dictionary=dict()
while True:
    try:
            ask1=int(input('how many students are there?'))
            ask2=int(input('how many asigments are there?'))
            for i in range(0,ask1):
                name=input('what is the name of the student?')
                minilist=[]
                for i in range(0,ask2):
                 value=int(input('what is the total value of the assignment?'))
                 grade=int(input('what is the grade the student got?'))
                 minilist.append(grade/value*100)
                 grades.append(grade/value*100)
                dictionary[name]=minilist
            print(dictionary)
            break
    except ValueError or ZeroDivisionError:
          print('please input a proper number when it is asked to do so.')
print(f'the mean of class grades,{statistics.mean(grades)}%')
print(f'the median of class grades,{statistics.median(grades)}%')
print(f'the mode of class grades,{statistics.mode(grades)}%')
while True:
 ask=input('would like to check the grade(s) of a specific student?')
 if ask=='y' or ask=='yes':
  print(dictionary[input('whoose grade(s) would you like to see?')])
 if ask=='n' or ask=='no':
    break