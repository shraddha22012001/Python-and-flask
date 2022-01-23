try:  
    a = 100
    b = "DataCamp"
    assert a == b
except AssertionError:  
        print ("Assertion Exception Raised.")
else:  
    print ("Success, no error!")