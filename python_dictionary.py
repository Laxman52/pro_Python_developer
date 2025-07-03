# Dictionary in Python
# dictionary stores data into key value pair
# dict -> key: value
# dictionary are unordered previously 3.6 and in previous version but now in 3.7 it is ordered
# mutable
# dynamic
'''
my_dict={
    "Name":"Laxman", "AGE":21, "Marks":98
}
print(my_dict)

# key must be unique

# how to add something to dictionary

my_dic1={
    'Fruites':{'Banana','Mango','Apple'},'Category':'Fruit'
}

my_dict['Price']=100
print(my_dict)

# to update existing element

my_dic2={
    'Fruites':{'Banana','Mango','Apple'},'Category':'Fruit','Version':2025
}

my_dic2['Version']=2026
print(my_dic2)

# to delete elements in dictionary

del my_dic2['Version']
print(my_dic2)


# Methods

# get

profile ={
    'Name':'Laxman','age':23,'Salary':1357865
}

age=profile.get('age','Not found')
print(age)

# keys method

keys=profile.keys()

print(list(keys))

# value method

value = profile.values()
print(list(value))

# items method(key:value)

all_items=profile.items()

print(all_items)

# pop method

popped = profile.pop('age','not found')

print(popped)
print(profile)

# to delete last item by default

print(profile.popitem())

# clear method

print(profile.clear())

'''
# dictionary comprehension

squares={x: x*x for x in range(1,6)}
print(squares)

# nested dicitionary

# we can store a dict inside a dict

