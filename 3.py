
set1 = {1,2,3,4,5,6,7,8,9,10}
list1 = list(set1)
list1.remove(3)
list1.remove(5)
list1.pop()
list1.pop()
list1.insert(0,5)
list1.insert(1,4)
list1.insert(2,6)
list1.insert(3,7)
print(list1)
print(list1[3:6])
set2 = set(list1)
print(set2)
del set2
sen1 = "adabe mard beh ze dolate oo"
list2 = sen1.split()
print(list2)
