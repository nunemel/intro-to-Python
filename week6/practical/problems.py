#1
class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def getDesc(self):
        print("A %s circle with radius %s." % (self.color, self.radius))  

circle = Circle(15, 'red')
circle.getDesc()   

#2
class MyClass:
    def __init__(self, my_str):
        self.my_str = my_str

    def get_String(self):
        return self.my_str 

    def print_String(self):
        print(self.my_str.upper())    

myClass = MyClass("aasada,ksh")
myClass.print_String()

#3
class Employee:
    def __init__(self, name, last_name, monthly_salary):
        self.name = name
        self.last_name = last_name
        self.__monthly_salary = monthly_salary 

    def getFullName(self):
        return  self.name + " " + self.last_name    

    def annualSalary(self):
        self.annual_salary = self.__monthly_salary * 12    
        if self.annual_salary > 100:
            return "High"
        else:
            return "Low"    

emp = Employee("Nune", "Melikyan", 10000)  
print(emp.getFullName(), emp.annualSalary())        

#4
class Car:
    def __init__(self, model, color, max_speed):
        self.model = model
        self.color = color
        self.max_speed = max_speed

    def compareCar(self, car2):
        self.car2 = car2
        if self.car2.max_speed < self.max_speed:
           return "car1 is better than car2"
        else:
            return "car2 is better than car1"     

car1 = Car("Subaru", "blue", 22223) 
car2 = Car("Bently", "red", 16223) 
print(car1.compareCar(car2))               

#5
class Police_car:
    def __init__(self, owner, price, pass_code):
        self.owner = owner
        self.price = price
        self.__pass_code = pass_code
        self.tax_value = 0.2

    def tax(self):
        return self.tax_value * self.price

    def greeting(self):
        if self.__pass_code.casefold() == "admin":
            print("Welcome to your car, %s" %self.owner)

    def setPassCode(self, pass_code):        
        self.__pass_code = pass_code

    def getPassCode(self):
        return self.__pass_code


carP = Police_car("Anna", 20000, "admin")   
carP.getPassCode()
carP.greeting()        

#6
#Assertions
#1
weekDays = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
def Alarm(day):
    if day.casefold() in weekDays:
        assert day == "sunday", "I won't wake you up today!"

Alarm("sunday")    
#2
def summary(x, y):
    assert isinstance(x, int) and isinstance(y, int) , "Arguments of type int required" 
    return x + y 

print(summary(1, 2))  
#summary("1", "2")    

#Exceptions
#1
def div1(x, y):
    try:
        if (not isinstance(x, int) or not isinstance(y, int)):
            raise TypeError
        if y != 0:
            return x/y
        else: 
            raise Exception 
    except TypeError:
        print("Type exception")          
    except Exception as ex:
         print(ex) 

     
div1(1, 0)     
#2
def div2(x, y):
    try:
        if (not isinstance(x, int) or not isinstance(y, int)):
            raise TypeError
        if y != 0:
            return x/y
        else: 
            raise ZeroDivisionError     
    except ZeroDivisionError as ex:
         print(ex) 
    except TypeError:
        print("Type exception") 
     
div2(1, 0) 

#3
myList = ['a', 0, 2]

try:
    for i in myList:
        print("The entry is:", i)
        reciprocal = 1/i 
        print("The reciprocal of %s is %s" % (i, reciprocal))
except ZeroDivisionError as zd:
    print("Oops!", zd)
except TypeError as te:
    print("Oops!", te)    

#4
try:
    username = input("Please enter username: ")
    if username == "Rambo":
        raise Exception
    print("Welcome, %s" % username)
except Exception:
    print("Rambo is an invalid username")    