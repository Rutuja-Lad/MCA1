# length ,append, extend, index, multiply on list

lst=[10,20,30,40,50]
print("Length of list is",len(lst))
lst.append(60)
print("Afetr adding element to the list: ",lst)
lst.extend([60,70])
print("After adding multiple element ot the list: ",lst)
print("Print element from 1 to 3",lst[1:4])
#Negative indexing
print("Print element in reverse",lst[::-1])