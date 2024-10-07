import math
def circleD(r):
 return (2*r)
def cylinderarea(r,h=10):
 return 2*math.pi*r*(r+h)
def conearea(r,h=10):
 return (math.pi*r*r)+(math.pi*r*math.sqrt(r**2+h**2))
def spherearea(r,h=10):
 return 4*math.pi*r*r
def circle(r,):
 return math.pi*r*r
def cylinder(r,h=10):
 return math.pi*r*r*h
def cone(r,h=10):
 return (math.pi*r*r*h)/3
def sphere(r,h=10):
 return (math.pi*r**3)*4/3
try:
    radius=int(input('what is the radius?'))
    print ('area of the cirlce is',circle(radius),'cm squared')
    print ('volume of the cylinder is',cylinder(radius),'cubic cm')
    print ('volume of the cone is',cone(radius),'cubic cm')
    print ('volume of the sphere is',sphere(radius),'cubic cm')
    print ('the diameter of the circle is',circleD(radius),'cm')
    print ('the surface area of the cylinder is', cylinderarea(radius),'cm squared')
    print ('the surface area of the sphere  is', spherearea(radius),'cm squared')
    print ('the surface area of the cone is', conearea(radius),'cm squared')
except ValueError:
 print('enter a number please')