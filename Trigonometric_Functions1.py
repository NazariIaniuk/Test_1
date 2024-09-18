import math
try:
 h=1.65
 Andgr=float(input('what is the angle of inclination in degrees'))
 Di=float(input('what is the distance from the tree in meters'))
 An=Andgr/57.2957795
 tree_height=(math.tan(An)*Di)+1.65
 #error and missuse stoppers
 if Di<=0:
    print('the formula does not work with numbers that low')
 elif Andgr<=0:   
    print('the formula does not work with numbers that low')
 else:
    print('height of the tree is', tree_height,'m' )
except ValueError:
 print('please inout a number')
