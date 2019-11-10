#HOMEWORK
import sys, argparse

#Lists:
a = [1, 4, 5, 7, 8, -2, 0, -1]
print(a[3], a[5])
a_sorted = sorted(a.copy(), reverse=True)
print(a_sorted[1:4], a_sorted[2:7])
a_sorted.pop(3)
a_sorted.pop(2)
print(a_sorted)
b = ["grapes", "Potatoes", "tomatoes","Orange", "Lemon", "Broccoli", "Carrot", "Sausages"]
b_sorted = sorted(b.copy())
c = a[1:4] + b[4:7]
print(c)

#Sets:
a1 = ["Cookies", "Chocolate", 8, True, -3, -5, "Chocolate", 8, False, 8]
b1 = [8, True, 10, 14, "Chocolate", "Milk", "Jelly", True, False, True]
set_a = set(a1)
set_b = set(b1)
union_ab = set_a.union(set_b)
intersection_ab = set_a.intersection(set_b)
union_ab.add("Kit-Kat") 
union_ab.add("Oreo") 
print(union_ab)
new_set = union_ab | intersection_ab 
print(new_set)
print("Chocolate" in new_set)
new_set.discard("Oreo")
print(new_set)

#Tuples:
t1 = (1, True, "a", -2, "Anna")
list1 = list(t1)
list1.pop(1)
t1 = tuple(list1)
print(t1)
t2 = (1, 2, 3, 4, 5)
listT = list(t2)
t3 = (list1[0], list1[1], listT[0], listT[1], listT[2])
print(t3)
print(t3[2])
t4 = [(1,3,5), (8,9), ("Anna", "Bob", "Alice")]
print(t4[0][1])

#Dictionaries:
market = {"dairy": ["yogurt", "cheese"],"fruits": 
    ["banana", "apple", "orange", "lemon", "apple", "banana", "banana"]}
print(market)
candies = ["mars", "kinder", "twix"]
market['candies'] = candies
print(market)

market.update({'fruits': sorted(set(market['fruits']))})
print(market)
 


