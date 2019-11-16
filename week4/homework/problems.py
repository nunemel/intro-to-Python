from IPython.display import clear_output

errorMessage = "Error: input must be an integer number."

def inputF(message):
    return input(message)  


#Conditionals
#1    
onePair = 100
inputMessage = "Please eneter how many pairs of shoes do you want to buy: "

while True:
    try:
        n_shoes = int(inputF(inputMessage))
        if onePair * n_shoes > 1000:
            print("You get a discount.")
        else:
            print("You don't get a discount.")  
        break      
    except ValueError:
        print(errorMessage)
        clear_output(wait = True)
        continue

#2
import statistics

d = {"name": "Armen", "age" : 15, "grades" : [10, 8, 8, 4, 6, 7]} 
if statistics.mean(d["grades"]) > 7:
    print("Good job")
else:    
    print("You need to work more.")  

#Loops and loop control statements
#3
for i in range(11):
    if (i % 2 == 0):
        continue
    print("odd =", i)

#4
list1 = [1, 3, 5, 7, 9, 11, 13, 15]
list2 = [4, 6, 14, 11,8, 16] 

for i in list1:
    print("i = ", i)  
    if i in list2:        
        break     

#5
from IPython.display import clear_output
menu = ['ice cream', 'chocolate', 'apple crisp', 'cookies']    
inputMessage = "Please enter any string: "   

while True:
    if inputF(inputMessage) in menu:
        print("Your desert will arrive in 10 minutes.")
        break
    else:
        print("Please choose another desert.")
        clear_output(wait = True)     

          
#List comprehension
#6
list2 = [1, 2, 3, 4, 5,  6, 7 , 222, 444, 15, 777, 888]
list2 = [x for x in list2 if x >= 5 and x <= 10]

print("list2 = ", list2, ",count = ", len(list2))

#7
list4 = [[10, 20, 40], [40, 50, 60], [70, 80, 90]]
list5 = [[100 if j == len(list4[i]) - 1 else list4[i][j] for j in range(len(list4[i]))] for i in range(len(list4))] 
print("list5 = ", list5)




