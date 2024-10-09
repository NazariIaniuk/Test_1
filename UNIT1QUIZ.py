x=0
while x==0:
    ask=int(input('''What would you like to solve:
     1) Area of Rectangle
     2) Times Tables
     3) Exit'''))
    if ask==1:
        w=int(input('select the width'))
        h=int(input('select the height'))
        ans=w*h
        print('the area of the Rectangle is',ans)
    elif ask==2:
        num=int(input('input a number'))
        for i in range(1,13):
            Ans=num*i
            print(i,'times', num,'is',Ans)
    elif ask==3:
        x=1