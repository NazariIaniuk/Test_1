def f(x):
 try:
     x=float(x)
 except ValueError:
        x="no"
 return x
print(f(input('enter a number')))
