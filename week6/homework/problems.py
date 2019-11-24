#1
import importlib
def moduleNotFoundFunc(moduleName):
    try:
        importlib.import_module(moduleName)
    except ModuleNotFoundError as mnf:
        print(mnf)
moduleNotFoundFunc("moduleName")        

#2
def div(x, y):
    try: 
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError
        assert y != 0, "Can't divide"
        return x/y
    except ValueError:
        print("Arguments must be of integer type")

print(div(1, 2))

import time

class Person:
    def __init__(self, name, last_name, age, gender, student, password):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student = student
        self.__password = password

    def countExecutionTime(func):
        def wrapper(*args, **kwargs):
            t1 = time.time()
            func(*args, **kwargs) 
            t2 = time.time() 
            print('execution time: ', t2 - t1)  
        return wrapper  

    @countExecutionTime
    def Greeting(self, second_person):
        if (isinstance(second_person, Person)):
             print("Welcome dear %s." %second_person.name)   

    def Goodbye(self):
        print("Bye everyone!")   

    def Favourite_num(self, num1):
        try:
            num1 = int(num1)
            print("My favourite number is %s" %num1)
        except ValueError:    
             print("Error: The num1 must be an integer.")        

    def Read_file(self, filename):
        try:
            open(filename + ".txt")  
        except FileNotFoundError as fnf:
            print(fnf) 
        except Exception as ex:
            print(ex)  

    def setPassword(self, password):
        self.__password = password

    def getPassword(self):
        return self.__password

person1 = Person("Anahit", "Poghosyan", 12, "female", True, "1213sdf")
person2 = Person("An", "Baboyan", 32, "female", True, "1213sdf")
person1.Greeting(person2)
person1.Goodbye()  
userInput = input("Please enter your favourite number: ")  
person1.Favourite_num(userInput)    
fileNameInput = input("Please enter the file name: ")
person1.Read_file(fileNameInput)