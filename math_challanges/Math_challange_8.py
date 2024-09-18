N=int(input('what n th number of the Fibonacci sequece you require?')) 
N-=1
B=1  
A=0
while N>0: 
  if A>=B:
     B=A+B
     N-=1
  elif B>A:
     A=A+B
     N-=1
if A>=B:
   print (B)
else:
   print(A)