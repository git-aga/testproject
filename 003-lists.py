# declare and creating lists
# I can change single element in list, in tuple not possible

list1 = list() #as function empty
list2 = [] #or in brackets empty

list3 = [1, True, "ABC", (200, "OK"), ["A", "B", "C"]] # I can mix elements in list, use diffrent variables
print(list3)
list3[1] = False # I can change single element in list, in tuple not possible
print(list3)

#add to list at the end
#append -  only one element at the end of list
list3.append(None) #methods colleareted with object so if list give you diffrent possibilities
print(list3)

#extend - marge one list with another
list3.extend([-3,-10,-20])
print(list3)
#insert data to: index where I want to add, new value); new elements shift right
list3.insert(0,"start")
print(list3)

"""pop - getout data from specific index, and return this value
remove value form list, we have to count position"""
v = list3.pop(2)
print(list3)
print(v)

#find element in list, 1st occurence is shown only; if there is no such value error occurs
print(list3.index("ABC"))
##how many occurence is fund, so if >0 you can procceed with index
"""if (list3.count("ABCD")) >0:
    print(list3.index("ABC"))
else:
    print("not found")"""

# remove all element from list; good to use this function if you don't list any more to release memory
#list3.clear()
#list3 = []
print(list3)
# reverse your list
list3.reverse() # cannot print(list3.reverse()) becouse it reverse and shows None or also wrong  list3=list3.reverse()
print(list3)

print("="*50) #make some string


# sort method cannot be used if you have diffrent typyes in your list
list4 = [10, 30, -20, 15, 23, 99, -199]
print(list4)
print("="*50) #make some string
#reverse sorting with reverse true
list4.sort()
print(list4)
list4.sort(reverse=True)
print(list4)
print("*"*50)
print("*"*50)


# how to copy list INVALID WAY!!!!!!
list1 = [1,2,5,10,20]
x = 10
y = x
y= 5
print(x)
print(y)
list2 = list1
list2[0]= -1 # OHHH NOOOOOO this change also value for list1, couse this is pointer that we copying,
print("lista1", list1)
print("lista2", list2)
# create clone, this is correct for "copying"
print("*"*50)
list2[0]= 1
list2 = list1.copy()
list2[0]= -1
print("lista1 orginal", list1)
print("lista2 cloned/copied", list2)

#indexing element in list and assigning elements
print("-"*50)
list_index  = [0, 1, 2, 3, 4, 5, 6, 7, 8 , 9]
print(list_index)
print(list_index[3])
print("index = 3 : ", list_index[3])
print("index = 8 : ", list_index[8])
print("value of the last index: ", list_index[9])
print("value of the last index: ", list_index[-1]) # the same as last, negativ index
print("second before the last element: ", list_index[-2])


