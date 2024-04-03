#Eccentricity for Ellipse
import math
a=float(input("Enter value of a: "))
b=float(input("Enter value of b: "))

if a>b:
    e=math.sqrt(((a*a)-(b*b))/(a**2))
    print("The eccentricity is : ",e)

elif a<b:
        e=math.sqrt(((b*b)-(a*a))/(b**2))
        print("The eccentricity is : ",e)

else:
      print('The eccentricity is 0')
      



