#  Tuple

# Q.1 Create a tuple with 5 numbers.
num=(1,2,3,4,5)
print(num)

# Q.2 Access the third element in a tuple
print(num[2])

# Q.3 Unpack a tuple into separate variables.
stu=("Aman","20","Male")
name,age,gender=stu
print(name)
print(age)
print(gender)



#    Sets

# Q.1 Create a set of 5 fruits.
fruits={"apple","banana","orange","grapes","mango"}
print(fruits)

# Q.2 Add a new fruit to the set.
add_fruit=fruits.add("papaya")
print("Added new fruits in set : ",fruits)

# Q.3 Remove an element from a set
remove_element=fruits.remove("apple")
print("Removed element from fruits : ",fruits)

# Q.4 Find Union of two sets.
set1={1,2,3,4,5}
set2={4,5,6,7,8}
union_set=set1.union(set2)
print("Union of two sets : ",union_set)

# Q.5 Find intersection of two sets.
intersection_set=set1.intersection(set2)
print("Intersection of two sets : ",intersection_set)

# Q.6 check if one set is subset of another.
subset=set1.issubset(set2)
print("Subset of set1 in set2 :",subset)

# Q.7 Convert a list with duplicate values into a set to remove duplicate.
num={1,2,2,3,4,4,5}
result=set(num)
print(result)



#   Dictionary

# Q.1 Create a dictionary storing student names and marks.
student={
    "Manthan":90,
    "Rahul":80,
    "Raj":70,
}
print(student)

# Q.2 Add a new key-value pair from an existing dictionary.
student["Aman"]=85
print(student)

# Q.3 Delete a key-value pair from a dictionary.
del student["Aman"]
print(student)

## Q.4 merge two dictionary into one.
dict1={
    "Manthan":90,
    "Rahul":80,
    "Raj":70,
}
dict2={
    "Aman":85,
    "Ankit":95,
}
dict3={**dict1,**dict2}
print(dict3)
#     OR
dict1.update(dict2)
print(dict1)

# Q.5 check if a key exists in a dictionary.
  # using if codition to find  key is exist in dictionary.
student={
    "Manthan":90,
    "Rahul":80,
    "Raj":70,
}
if "Manthan" in student:
    print("key exist")
else:
    print("key not exist")

# Q.6 Count word frequency in a given string using a dictionary.
str="apple banana orange apple"
word=str.split()
freq={}
for i in word:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

# Q.7 find the key with the maximum value in a dictionary.
marks={
    "Aman":90,
    "Rahul":80,
     "Raj":70,
}
max_key=max(marks,key=marks.get)
print(max_key)

# Q.8 Revrse keys and values in a dictionary.
student={
    "Manthan":90,
    "Rahul":80,
    "Chandan":99,
}
reverse={}
for key, values in student.items():
    reverse[values]=key
print(reverse)

# Q.9 Update the values for a specific dictionary
student={
    "Manthan":90,
    "Rahul":80,
    "Raj":70,
}
student["Raj"]=99
print(student)

# Q.10 convert a list of tuples into a dictionary.
data=[("Aman",90),("Rahul",80),("Raj",95)]
print(data)
student=dict(data)
print(student)
