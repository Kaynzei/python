#to extend or make list longer,
list1 = [4, 2, 1, 5, 3]
list2 = ['banana', 'apples', 'mango', 'oranges']
#list1.extend(list2)
print(list1)
#to append list2
list2.append('cherry')
print(list2)
#to put insert or make amendment on a definite position or in-between a list
list2.insert(1, 'cherry')
print(list2)
#to remove from the list
list2.remove('banana')
print(list2)
#to delete a list
#list2.clear()
print(list2)
#to print the index number of mango
print(list2.index('mango'))
#to know the number of times an item is appearing on the list
print(list2.count('cherry'))
#to print a list in ascending order
list1.sort()
print(list1)

# to print from behind
list2.reverse()
print(list2)
#to duplicate a list, just create a new list ,call it list3
list3 = list2.copy()
print(list3)

#to delete the last thing we have in list2
list2.pop()
print(list2)
#we can also be specific in removal like
list2.remove('oranges')
print(list2)
#another way of deleting is 
del list2[0]
print(list2)