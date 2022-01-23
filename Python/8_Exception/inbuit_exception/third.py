class Attributes(object):
    x = 2
    print (x)

try:
    object = Attributes()
    print (object.attribute)
except AttributeError:
    print ("Attribute Exception Raised.")