x = input("Enter the plane's take off speed in m/s:")
y = input("Enter the plane's acceleration in m/s**2:")
v = int(x)
a = float(y)
r = (v**2)/(2*a)
print("The minimum runway length needed for this airplane is",r,"meters")