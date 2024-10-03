import math
def circleD(r):
 D=2*r
 return D
def cylinderarea(r,h=float(10)):
 A=2*math.pi*r*(r+h)
 return A
def conearea(r,h=10):
 A=(math.pi*r*r)+(math.pi*r*math.sqrt(r**2+h**2))
 return A
def spherearea(r,h=10):
 A=4*math.pi*r*r
 return A
def circle(r,):
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
print ('area of the cirlce is',circle(radius),'cm squared')
print (' volume of the cylinder is',cylinder(radius),'cubic cm')
print ('volume of the cone is',cone(radius),'cubic cm')
print ('volume of the sphere is',sphere(radius),'cubic cm')
print ('the diameter of the circle is',circleD(radius),'cm')
print ('the surface area of the cylinder is', cylinderarea(radius,'cm squared'))
print ('the surface area of the sphere  is', spherearea(radius,'cm squared'))
print ('the surface area of the cone is', conearea(radius,'cm squared'))