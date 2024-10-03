def money(x,y=5):
 y=y/100
 x+=x*y
 return x
cash=int(input('how much to invest?'))
interestrate=int(input('what is the interest rate in %?'))
print(money(cash,interestrate))