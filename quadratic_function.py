import math


a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
delta = (b*b) - 4 * a * c
if delta > 0:
    x1 = (-b-math.sqrt(delta))/2*a
    x2 = (-b+math.sqrt(delta))/2*a      
    print (delta)
    print (x1)
    print (x2)
elif delta == 0:
    x = -b/2*a
    print (x)
else:
    print ("Brak miejsc zerowych")




