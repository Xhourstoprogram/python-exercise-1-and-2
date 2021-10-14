x = int(input("Enter the mass of the cart (in kg): "))
y = int(input("Enter the force to push the cart (in N): "))
m = (x)
F = (y)
g = 9.8
import math
sin = F/(m*g)
print("The angle of the ramp is",math.degrees(sin),"degrees")