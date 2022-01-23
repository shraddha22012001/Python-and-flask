#Write a Python function which accepts two arguments x and y and returns (x + y) * (x + y).
def nsquare(x, y):
   return ((x+y)**2)

a = int(input("Enter First Number :"))
b = int(input("Enter Second number:"))
print("The square of the sum of is : " ,nsquare(a,b))
