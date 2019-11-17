#Functions
def errorRaiseFunc(type):
    raise Exception('The argument must be of %s type.' %type)

#1
def funcMean(int1, int2, int3):
    """ Counts the mean of three integer parameters. """
    if not isinstance(int1, int) or not isinstance(int2, int) or not isinstance(int3, int):
        errorRaiseFunc(int)

    return (int1 + int2 + int3)/3
      
print("mean =", funcMean(1, 2, 3)) 

#2
def funcEvenList(listParam):
    if not isinstance(listParam, list):
         errorRaiseFunc(list)
    return len([i for i in listParam if isinstance(i, int) and i % 2 == 0])

print("count =", funcEvenList([1, 2, 4, 5, 6]))

#3
import re 
def checkPassword(password):
    return (len(password) >= 10 and bool(re.match("(.*\\d.*){2,}", password)))
     
print(checkPassword("ASASS1nn23AAA"))

#4
def funcGreeting(name, greeting = "Welcome to our company!"):
    print("%s, %s" % (name, greeting))
funcGreeting("Nune")

#5
import statistics
def funcGrades(name, *args):
    if (len(args) < 1 or len([i for i in args if isinstance(i, int)]) != len(args)):
        print("No grades available for %s" % name)
        return

    print("%s​, your average grade is: ​%d​" % (name, statistics.mean(args)))
        
funcGrades("Nune", 1, 2, 3)
funcGrades("Ann", 55)              

#6
def fun1(user, **kwargs):
    if user == "admin":
        for key, value in kwargs.items():
            print("%s: %s" % (key, value))
    else:
        print('Access denied to the user %s' % user)     

fun1("admin", name = "Poghos", surName = "Poghosyan")        


#7 are in other files

#8
#Decorators
list1 = ['Anna', 'Edgar']
def decorator(func):
    def wrapper(*args):
        print('before calling the function list1', list1)
        print('after calling the function list1', func(*args))
    return wrapper

@decorator
def add_values(list2):
    if (not isinstance(list2, list)):
        errorRaiseFunc(list)

    return list1 + [i for i in list2 if i not in list1]     

add_values(['Anna', 'Edgar', 'Poghos', 'Suzie', 'AAA', 'Bbb'])

#9
def addText(func):
    def wrapper():
        return func().capitalize() + "!!! Welcome to the party."
    return wrapper 

def makeLowercase(func):
    def wrapper():
       return func().lower()
    return wrapper      

@addText
@makeLowercase
def funcDec():
    return "HI EVERYONE"

print(funcDec())    

#Generators
#10
def list_func(list1):
    if not isinstance(list1, list):
        errorRaiseFunc(list)

    return (i for i in list1)

#11
def iter_num(n):

    if not isinstance(n, int):
        errorRaiseFunc(int)

    return (i for i in range(1, n + 1))

#12
def power(max):

    if not isinstance(max, int):
        errorRaiseFunc(int)
    return (i*2 for i in range(max + 1))        

gen1 = list_func([1, 2, 3, 4, 5, 6])
print(next(gen1))
gen2 = iter_num(3)        
print(next(gen2))
gen3 = power(3)
print(next(gen3))

