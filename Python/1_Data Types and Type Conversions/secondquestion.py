#Write a Python program to get the largest number from a list.
def myMax(list1):
    max = list1[0]
    for x in list1:
        if x > max :
             max = x
    return max

list1 = [10, 20, 4, 45, 99]
print("Largest element is:", myMax(list1))