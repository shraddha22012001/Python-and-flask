#Write a Python program to concatenate all elements in a list into a string and return it.
def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data([1,2,3,4,5,6]))