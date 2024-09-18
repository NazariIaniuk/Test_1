import math as mth
r=float(input('what is the radius of the cyliner top part in centimeters'))
h=float(input('what is the height of the cyliner in centimeters'))
A=(2*mth.pi*r*h)+(2*mth.pi*r**2)
V=(mth.pi*r**2*h)
print(V,'is the volume of the Cylinder in cm^3')
print(A, 'is the surface area of all sides of the cylinder in cm^2')
