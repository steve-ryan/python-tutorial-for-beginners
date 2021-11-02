#unlike lists,sets cannot contain lists or dictionaries

#Curly braces with atleast one value , if no value this creates a dictionary instead
example_set = {123}

#To have empty set using set function
#using this function you can provide a list of objects
example_set2 = set([123])

#using 'in' keyword to check if object is present in a list
a = 123 in example_set
print(a)

#updating a set
update_set = set()
##we use .add
update_set.add(1234)
print(update_set)