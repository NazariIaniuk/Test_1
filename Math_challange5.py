#F = °C × (9/5) + 32   C = (°F - 32) × 5/9
formula=int(input('type 1 to convert Celsius to farhenheit and type 2 if you want to convert farhenheit to Celsius'))
if formula==1:
 Celsius=float(input('enther the teperature in Celsius'))
 Fahrenheit=Celsius*(9/5)+32
 print(Celsius,'Celsius is',Fahrenheit,'Fahrenheit')
elif formula==2:
 Fahrenheit=float(input('enther the teperature in Celsius'))
 Celsius=(Fahrenheit-32)*(5/9)
 print(Fahrenheit,'Fahrenheit is',Celsius,'Celsius')
else:
 print('please restart the program and pick a valid option')