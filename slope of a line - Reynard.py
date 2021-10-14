a = input("Enter the x coordinate for point 1 :")
b = input("Enter the y coordinate for point 1 :")
c = input("Enter the x coordinate for point 2 :")
d = input("Enter the y coordinate for point 2 :")
x1 = float(a)
x2 = float(c)
y1 = float(b)
y2 = float(d)
dy = y2 - y1
dx = x2 - x1
slope = dy / dx
print("The slope for the line that connects two points",(x1,y1),"and",(x2,y2) , "is", (slope) )