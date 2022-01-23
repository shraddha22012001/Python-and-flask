import re
class Country:
    AVG_POPULATION = 100
    def __init__(self, country_name, country_code):
        try:
            self.country_name = country_name
            self.country_code = country_code
            if not re.findall(r'^[a-zA-Z]+$', country_name) or not re.findall(r'^[a-zA-Z]+$', country_code):
                  raise ValueError()
            else:
                try:
                     if len(country_code) != 3:
                       raise ValueError(country_code)
                     print("entered values are Valid ")
                     print("country Name :",self.country_name)
                     print("country Code :",self.country_code)
                except ValueError:
                       print("Please enter  country code of length 3")
        except ValueError:
             print("Plese enter valid country name and country code ")
    @property
    def formatted_country_name(self):
        return self.country_name +' ('+ self.country_code+')'
    @formatted_country_name.setter
    def formatted_country_name(self, vals):
        c_n,c_c = vals
        self.country_name = c_n
        self.country_code = c_c
    
    @formatted_country_name.deleter   
    def formatted_country_name(self):
        print('Deleting..')
        del self.country_name
        del self.country_code

    def country_short_form(self, cn):
        try:
            if not re.findall(r'^[a-zA-Z]+$', cn):
               raise ValueError()
            txt = cn[:2]
            return txt.upper()
        except ValueError:
             print("Plese enter valid country name  ")
    def is_densly_populated(self, population):
            if population > self.AVG_POPULATION:
                return True
            else:
                return False
    @staticmethod
    def world_avg_population(country_pop):
        sum = 0
        for i in country_pop:
            sum += i
        return sum/len(country_pop)

        



       
country_name = input("Enter country name :")
country_code = input("Enter country code :")
while True:
  ch = int(input('''Select Operation you want to perform: 
              1.To check Country name and code are valid
              2.To check Country short form
              3.To Check Population is densly or not
              4.To calculate average of all country population
              5.To Perform getter setter and deleter on object
              6.exit()
              Enter your Choice:'''))
  if ch == 1:
      obj = Country(country_name,country_code)
  elif ch == 2:
      print("Country Short Form :",obj.country_short_form(obj.country_name))
   
  elif ch == 3:
      population = input('Enter Population :')
      try:
          val = int(population)
          check = obj.is_densly_populated(val)
          if check:
             print('it is densly populated')
          else:
             print('it is not densly populated')
      except ValueError:
             print('Only integers are allowed')
  elif(ch == 4):
       list = [100,34,456,600,500]
       print('Average of Population of all countries :',Country.world_avg_population(list))
  elif ch == 5:
        print('Formated Country Name is ', obj.formatted_country_name)
        obj.formatted_country_name = ('Indio','par')
        print('Formated Country Name is ', obj.formatted_country_name)
        del obj.formatted_country_name
       # print("deleting",obj.country_name)
  elif ch == 6: 
      exit()
  else:
    print("enter valid choice")