def f(x):
 try:
     x=float(x)
 except ZeroDivisionError:
        x="no"
 return x
print(f(input('enter a number')))
