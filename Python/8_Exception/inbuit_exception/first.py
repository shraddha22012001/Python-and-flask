try:  
    a = 100 / 0
    print (a)
except ZeroDivisionError:  
        print ("Zero Division Exception Raised." )
else:  
    print ("Success, no error!")