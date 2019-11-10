list5 = [34, 45, 67, 89, 45, 87]
list6 = list5.copy()
print("before the change", list6)
list6.pop(5)
list6.pop(4)
list6.pop(0)

print("after the change", list6)
print("list5 = ", list5)