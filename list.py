name = ['ken','sam','antony']
list("wachira")

# split
print("hello am steve wachira." .split("ac"))
# print name
# print test

# adding list
cuzo = ['shifrah','shikoh']
cuzo.append('bilhah')
print(cuzo)

#add list .insert()
test_point = [90,87,17,56]
test_point.insert(1,50)
print(test_point)

#extend
test_point = [90,87,17,56]
test_point_2 = [12,5,8,6,31]
test_point_2.extend(test_point)
print(test_point_2)

#remove item
test_point_2 = [125,90,87,12]
test_point_2.pop()
print(test_point_2)


#remove specific index
test_point_2 = [1,2,3,4,5,6]
test_point_2.pop(3)
print(test_point_2)

#object in list
test_point_2 = [1,2,3,4,5,6]
print(60 in test_point_2) #60 not appearing on the string
print(test_point_2.count(2)) #2 appears once
print(max(test_point_2)) #maximum value on the list
print(len(test_point_2)) #length of the list
print(sum(test_point_2)) #sum of list object and works for both int & float


#A list can contain lists
marks = [67,78,50,28]
cat = [12,30,2]

total_marks = [marks,cat]
print(total_marks)
print(len(total_marks))

#accesing nested objects
print(total_marks[0][1])

#getting index of an object
marks_tips = [12,78,10]
print(marks_tips.index(78))

#sort list objects
marks_tips.sort()
print(marks_tips)