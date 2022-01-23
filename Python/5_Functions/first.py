#Write a function in a Python program to compute the greatest common divisor (GCD) of two positive integers.

def gcd(x, y):
 z = x % y
 while z:
   x = y
   y = z
   z = x % y
 return y
print("GCD of 12 & 19 =",gcd(12, 19))
print("GCD of 2 & 6 =",gcd(2, 6))
print("GCD of 45 & 20 =",gcd(45, 20))