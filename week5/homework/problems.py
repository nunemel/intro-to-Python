def errorRaiseFunc(type):
    raise Exception('The argument must be of %s type.' %type)

#1
def funcMax(*args):
    if len(args) == 0 or len([i for i in args if isinstance(i, int)]) < 1:
        return "no numbers are given"
    max = 0
    for i in args:
        if i > max:    
            max = i
        return max

print(funcMax(1, 334, 45, 778, 3))      

#2
def uniqueList(list1):

    if not isinstance(list1, list):
        return

    if isinstance(list1, list):
        #null list
        uniqueList = []
        for i in list1: 
            # checks if exists in uniqueList or not 
            if i not in uniqueList: 
                uniqueList.append(i) 
        return uniqueList

print(uniqueList(['Anna', 'Bob', 'Anna', 'Helen', 'Kat', 'Susie', 'adfasf', 'Helen']))

#3
def decorator(func):
    def wrapper():
        print("Before the function call")
        print(func())
        print("After the function call")
    return wrapper    

@decorator
def func1():
    return "Inside the function"

func1()

#4
def decText(func):
    def wrapper():
        return func() + ", it's me!"
    return wrapper    

def docU(func):
    def wrapper():
        return "<u>" + func() + "</u>"
    return wrapper

@docU
@decText
def funcDef():
    return "Hi"

print(funcDef())

#5
def my_range(n):
    if (not isinstance(n, int)):
        errorRaiseFunc(int)
    return ("there are no values left" if i == n + 1 else i for i in range(n + 2))  

for i in my_range(5):
    print(i)   

