import re

class NameNotValid(Exception):
    
    def __init__(self, name, message="name is not valid"):
        self.name = name
        self.message = message
        super().__init__(self.message)

class AgeNotValid(Exception):
    
    def __init__(self, age, message="Age is not valid"):
        self.age = age
        self.message = message
        super().__init__(self.message)
class emailNotValid(Exception):
    
    def __init__(self, email, message="email is not valid"):
        self.email = email
        self.message = message
        super().__init__(self.message)

class phoneNotValid(Exception):
    
    def __init__(self, phone, message="phone is not valid"):
        self.phone = phone
        self.message = message
        super().__init__(self.message)   
class Person:
        age = 0
        phone = 0000000000
        email =  ''
        name =  ''
        def input_info(self):
          age = int(input("Enter age: "))
          if  age <= 0:
            print(AgeNotValid(age))
          else :
              name = input("Enter Name: ")
              if not re.findall(r'^[a-zA-Z]+$', name):
                print(NameNotValid(name))
                return False
              else:
                email = input("Enter Email: ")
                if not re.findall(r'^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$',email):
                  print(emailNotValid(email))
                  return False
                else:
                  phone = input("Enter phone: ")
                  if not re.findall(r'^[0-9]{10}',phone):
                      print(phoneNotValid(phone))
                      return False
                  else:
                      self.age = age
                      self.name = name
                      self.email = email
                      self.phone = phone
                      return True


list = []

ch = 1
while(ch):
  p = Person()
  x = p.input_info()
  if x :
     list.append(p)
     print("person data inserted sucessfully")
  else:
      print("Please enter valid data")
  ch = int(input("if you want to continue enter '1' or '0' to exit:"))

for obj in list:
         print("name :"+ obj.name + " phone  : " + str(obj.phone)+" age  : "+str(obj.age)+" email : " +obj.email)

