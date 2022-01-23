#Writea Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string.
def string_b_ends(str):
  if len(str) < 2:
    return 'empty'

  return str[0:2] + str[-2:]

print(string_b_ends('w3resource'))
print(string_b_ends('w3'))
print(string_b_ends('w'))