# Create a function that takes a date string as an input and checks if it is of the format Month date, year. The month must be the full month name and date must have 0 padding (01) and year must have full year.

import re
str = input("enter date: ")  # Given input
l = str.split(" ")

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
l[1] = l[1][:-1]
if l[0].lower() in months and re.findall("[0-3][0-9]", l[1]) and len(re.findall("\d", l[2])) == 4:
    
    if (months.index(l[0].lower())+1) == 2 :
        if int(l[2]) % 400 == 0 and int(l[1]) <= 29:
            print("Date is Valid")
        elif int(l[2]) % 400 != 0 and int(l[1]) <= 28:
            print("Date is Valid")
        else:
            print("Date is not Valid")
            
    elif (months.index(l[0].lower())+1) % 2 == 0 and (months.index(l[0].lower())+1) != 2:
        if int(l[1]) <=30:
            print("Date is Valid")
        else:
            print("Date is not Valid")

    elif int(l[1]) <=31 and (months.index(l[0].lower())+1) != 2:
        print("Date is Valid")
        
    else:
        print("Date is not Valid")
    
else:
    print("Date is not Valid")