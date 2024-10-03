import math
def cirle(r,):
 A=math.pi*r*r
 return A
def cylinder(r,h=10):
 V=math.pi*r*r*h
 return V
def cone(r,h=10):
 V=(math.pi*r*r*h)/3
 return V
def sphere(r,h=10):
 
 
 V=(math.pi*r**3)*4/3
 return V
radius=float(input('what is the radius?'))
print ('area of the cirlce is',cirle(radius),'cm')
print (' volume of the cylinder is',cylinder(radius),'cm')
print ('volume of the cone is',cone(radius),'cm')
print ('volume of the sphere is',sphere(radius),'cm')