#1
n1 = input("Please enter any integer value: ")
n2 = input("Please enter any integer value: ")

max = 0
if (n1 > n2):
    max = n1
else:    
    max = n2
print("The number %s is the greatest." % max)    

#2
a = 12
b = 12
if a == b:
    print("square")
else:
    print("rectangle")

#3
name = "Anna"
age = 14
password = "blabla"     

if name == 'Batman':
    print("Welcome Mr. Batman!")

if (age < 16):
    print("Dear %s, you are too young to register" % name)  

if (not ('*' in password) or not('&' in password)):
    print("Please enter a different password")

#Loops
#5
for i in range(101):    
    if (i % 2 == 1):
        print("i = ", i)

#6
for i in range(7):
    if (i == 2 or i == 4):
        continue
    print(i)    
#7
for i in range(1, 21):    
    if (i % 3 == 0 and i % 5 == 0):
        break
    print(i)    
#8
list1 = [5, 7, -7, 'abc', 2, 4, True, 3, 4, 6, 7, 7]
for item in list1:
    if (item == 3):
        break
    print (item)    

#9
from IPython.display import clear_output

correct_num = 5
inputMessage = "Please guess an integer number: "
errorMessage = "Input must be an integer number, please enter again:"
#checks if the input is correct if it is correct prints it else clears the previous output and asks to enter the number again
count = 0
for i in range(10):
        try:
            #clears the previous output
            clear_output(wait = True)
            guess = int(input(inputMessage))
            #checks if the input is odd
            if (guess == correct_num):
                print("That was a good guess!")
            else: 
                continue    
            break
        except ValueError:
            inputMessage = errorMessage
            clear_output(wait = True)
            continue


#List comprehension
#10
num = [7, 8, 120, 25, 44, 20, 27]
print("before change num =", num)
newList = [x for x in num if x % 2 == 1]
print("after change num =", newList)

#11
list3 = [ x**2 for x in range(1, 51)]
print("list3 = ", list3)

#12
list1 = [1, 14, 123, 45, 56, 78, 23 , 11]
list2 = [ x for x in list1 if x > 20]
print("list2 = ", list2)

#13
str1 = input("Please enter any string: ")
print("str1 = ", str1)
myList = [x for x in str1]
print("myList = ", myList)

#14
list1 = ['a', 'abc', 'xyz', 's', 'aba', '1221']
newList = [x for x in list1 if len(x) >= 2 and x[0] == x[-1]]
print(newList)