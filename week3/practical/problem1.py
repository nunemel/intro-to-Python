import sys

list1 = ["hello", 1, True] 
print("before the change", list1)
list2 = sys.argv[1:]
list1.extend(list2)
print("after the change", list1)