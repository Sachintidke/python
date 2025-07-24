#Implement a python program to perform following operations on the list:
# 1. Create a List
# 2. Access a List
# 3. Update a List
# 4. Delete a List
# 5. Add a list

# Using Squanre Brackets
# List can cotain duplicate items.
# List in python are mutable. Hence, We can modify, replace or delete the items.
# List are ordered.It maintain the orderof elements based on how they are added.
# Accessing items in list can be done directly using their position (index), sterting from o.



# 1. Create a list

#list of integer
list = [87, 67, 86, 77, 87]
print(list)

#list of strings
fruits = ['mango', 'banana', 'cherry', 'apple']
print(fruits)

#list Items for different type
student = ['sachin', 33, 'computer engineering', 75.88]
print(student)

#an empty list
empty_list = []
print(empty_list)

#Create a list [8, 8, 8, 8, 8, 8+]- repeated list 
S = ["sachin"] * 10
print(S)



# 2. Access List

list1 = [87, 67, 86, 77, 87]
print(list1 [2])
print(list1 [-1])


# 3. Update List

list3 = [87, 67, 86, 77, 87]
list3[2] = 76
print(list3)



# 4. Delete lis
# remove(): Remove the first occurrence of an element.
# pop(): Remove the element at a specific index or the last elementg if no index is specified.
# del statement(): Deletes an element at a specified index.


list4 = [87, 67, 86, 77, 87]
list4.remove(77)
print(list4)

list4 = [87, 67, 86, 77, 87]
list4.pop(3)
print(list4)

list4 = [87, 67, 86, 77, 87]
del list4[-3]
print(list4)




# 5. Adding element into list

# We can add element to a using the following method:
#  Append(): Adds an element at the end of the list.
#  Extenf(): Adds multiple element to the end of the list.
#  Insert(): Adds an element at a specific position.


B = []

# Adding 75 to end of list
B.append(75)
print(B)

# Adding multiple element [12, 13, 23] at the end
B.extend([30, 40, 50])
print(B)


# Inserting 5 at index 0
B.insert(2, 50)
print(B)