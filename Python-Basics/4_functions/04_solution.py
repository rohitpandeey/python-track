import math
def arr(radius):
    area= round(math.pi*radius*radius,1)
    circumferace=round(2* math.pi*radius,1)
    return area,circumferace

a,c=arr(5)
print("area:",a,"circum",c)