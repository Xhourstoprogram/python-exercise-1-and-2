a = int(input("Enter the temperature in Fahrenheit: "))
while a < -58 or a > 41:
    print("Temperature must be between -58F and 41F")
    a = int(input("Please re-enter the temperature in Fahrenheit: "))
b = int(input("Enter the wind speed miles per hour: "))
while b < 2:
    print("Speed must be greater than or equal to 2")
    b = int(input("Please re-enter the wind speed miles per hour: "))
twc = 35.74 + (0.6215*a) - (35.75*(b**0.16)) + (0.4275*a*(b**0.16))
c = float(twc)
print(f"\nThe wind chill is {c:.3f}")