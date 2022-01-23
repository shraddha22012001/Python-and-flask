try:  
    a = {1:'a', 2:'b', 3:'c'}  
    print (a[4])  
except LookupError:  
    print ("Key Error Exception Raised.")
else:  
    print ("Success, no error!")