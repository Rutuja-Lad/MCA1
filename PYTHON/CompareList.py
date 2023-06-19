#program to compare the lists
list1=["3,7,9,4"]
list2=["3","2","4","1"]
list3=["1","2","3","4"]
list1.sort()
list2.sort()
list3.sort()

if list1==list2:
    print("List1 and List2 are same")
else:
    print("List1 and List2 are not same ")    
if list2==list3:
    print("list2 and list3 are same")
else:
    print("list2 nad list3 are not same")        