# list in a python is a collection of items (like number, strings) that is ordered , mutable, and allow duplicates.

# why we use it 
# in list we can store multiple values 
# to group related data
# to easily iterate,update,or manipulate collections of data
#  How List is Different from a Variable?
# Feature	Variable (int, str)   	List (list)
# Stores	Single value	       Multiple values
# Syntax	x = 5	               lst = [1, 2, 3]
# Mutable	No	                   Yes (can change items)
# Indexed	Not applicable	       Yes (0-based index)


# here we can store hetrogenus data 

# how to make a list in different ways 
'''

my_list1= [1,2,45,"Laxman","Placed","Hardworking"]
print(my_list1)

# or by using list constructor


my_list2= list((1,2,45,"Laxman","Placed","Hardworking"))
print(my_list2)



# to update list element we can use indexing
my_list2= list((1,2,45,"Laxman","Placed","Hardworking"))
print(f'before updating list{my_list2}')
my_list2[0]='Varun'
print(f'Updated list{my_list2}')

# if we want to update multiple elements in one go than we can use range indexing

my_list2= list((1,2,45,"Laxman","Placed","Hardworking"))
print(f'before updating list{my_list2}')
my_list2[0:3]=122,456,777
print(f'Updated list{my_list2}')


# concatenation of two list

l1=[1,23,4,5,6,7]
l2=[34,67,9,9076,4,3]

print(l1+l2)

# we can repeat our list here list is only one time created but its element is repeated given no of times

print(l2*5)

# membership operator used for searching

# IN ,  NOT IN

l12=[12,2,3,4,4,5,5,6]
check=int(input("Enter no to be searched: "))
if check in l12:
    print('Found')
else:
    print('Not Found')

l12=[12,2,3,4,4,5,5,6]
check=int(input("Enter no to be searched: "))
if check not in l12:
    print('Not Found')
else:
    print('Found')


# Alias concept

list12=[1,23,45,5]
lis23=list12
print(lis23)

# in alias here is a problem like if we change in lis23 it will AUTOMATICALLY change in both of the list so to avoid this we can use cloning method

list232=[1,23,45,5]
lis233=list12.copy()
lis233[0]=123
print(lis233)
print(list232)

'''
# Methods of list 

# append method - if we use to add something to the list then by default the added thing will be at the last always

name=[100,234,678,543,467]
name.append(3456)
print(name)

# extend method = append at the last of the list on extend method is applied


name2=[23,45]

name2.extend(name)
print(name2)

# insert method = by using indexing in arguments of this function we can add any where in list


ins=[2,35,6,8,9,0,765,43]
ins.insert(4,"I know python list very well")
print(ins)

# remove method (directly deletes value)

ins.remove(35)
print(ins)


# for deleting using indexing use pop

c=[235,456,43,345,345,6]
popped=c.pop(5)
print(c)

# if want to clear a list at one go then use clear() method

c.clear()
print(c)

# if you want to know the index of some value in list simply use index method

index=ins.index(0)
print(index)

# to get the count the occurence of some thing in list directly use count method

counter=c.count(345)
print(counter)

# to sort data of list use sort function

ab=[77,8,9,6,444,78,54,3,-6,75,-6,-564,605,-67]
ab.sort()
print(ab)

# reverse method

ab.reverse()
print(ab)

# practise quesiton 

# finding min and max in list

ab233=[77,8,9,6,444,78,54,3,-6,75,-6,-564,605,-67,45,677,54,56,45,6]

# min and max function
print(min(ab233))
print(max(ab233))

# find common elements of list [intersection method]
ab45=[77,8,9,6,444,78,54,3,-6,75,-6,-564,605,-67]
ab46=[77,8,9,6,444,-67]

# set function

s1=set(ab45)
s2=set(ab46)

s3=s1.intersection(s2)
print(list(s3))

# nested list


ab467=[77,8,9,6,444,-67,[3556,754,3,654,23,45,7]]
print(ab467)


# range function
# start , stop , step - used in int data only


number=list(range(1,23,4))
print(number)

# list comprehension

squares=[]

for i in range(1,23):
    squares.append(i ** 2)
print(squares)

