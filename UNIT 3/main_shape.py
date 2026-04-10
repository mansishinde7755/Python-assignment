Main_shape.py
import shape
print("choose shape :")
print("1.Circle")
print("2.Rectangle")
print("3.Triangle")

Choice = float(input("Enter your choice (1-3):"))

if Choice == 1:
    r = float(input("enter radius:"))
    area = shape.area_circle(r)
    print("Area of circle =", area)

elif Choice == 2:
    l = float(input("enter length:"))    
    w = float(input("enter width:"))
    area = shape.area_rectangle(l,w)
    print("Area of rectangle =", area)

elif Choice == 3:
    h = float(input("enter height:"))    
    b = float(input("enter base:"))
    area = shape.area_triangle(h,b)
    print("Area of triangle =", area)

else :
    print("Invalid choice")