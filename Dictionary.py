# Dictionary 
# 1. Dictionary Annoted by {curly brackets}
# 2. Dictionaryn are combination of multiple 
# keys: values 
# 3. Dict are mutable.
 # 4. Dict are Hetrogenous
# 5 in dict keys will be unique but values can be duuplicate. 
# 6 Dict are ordered 
# """"""

# d = {1:10,2:20,3:30}
# print(d[2])

# d= {1:10 , 2:20,3:30}
# d [4] = 100 # creating a new key :value pair which never exists 
# print(d)
# d = {1:10,2:20,3:30}
# print(d)

# D = {1:10,2:20,3:30}

# for i in d:#->1
#     print(i,d[i])#1 , d[1]


# Methods in dict
#1 .. keys ()
# d = {"Ravi : 80, "Rohan":23, "Devraj":80}
#      print (d.keys())
# #2 .. value ()
# print(d.values())
# #4.. pop()-> key and remove both key nand value
# print(d.items())
# print(d)
# #4..pop () -> key and removes both key and value.
# d.pop("Rohan")
# print(d)

#.get () -> agar key present hai in dictionary so we will get value for that key either 


# update ()-> merge two dictionaries
# a={1:10,2:20,3:30}
# b={4:40,5:50,6:60}
# a.update(b)
# print(a)


# for key, valye 
#question keys print
# d = {"Ravi":70,"Abhishek":33,"Rohan":12}
# print(d.keys())

# find the total of maks without using sum ()
# d = {"Ravi":70,"Abhishek":33,"Rohan":12}
# for i in d.values():#i->70
#     total = total +i
# print(total)    

#print student who scored more than 50
# d = {"Ravi":70,"Abhishek":33,"Rohan":12}
# for i in d.keys(): 
#     print(i)
#  i:f maks > = 50:

# que find the student with the highest marks 
# d= {"Ravi":70,"Abhishek":33,"Rohan":12}
# top = 0 #ravi 
# highest = 0 
# for name, makes in d.itms()
#     if marks > highest:
#         highest = marks  
#         top = name 
#print(top,highest)
# add bonus 5 marks every student
""
# Sets 
# 1.sets are annoted {} or set()
# ""'
# s = {} # dict
# s = set () # empty set
# s = {1,1,2,2,3,3,4,5} repart not count
# print(s)

#2 sets are annoted by {} or set {}
# s = {1,2,3,3,4,4,5,5,70.2,"sample"}
# print(s)

# sets are inorderd that means there is no indexing in sets 

#5 sets are semi - mutable 
#list to set 
# l + [1,1,2,3,4,5]
# print(set(l))
#1..add()-> adds an element to set.
# s = {1,2,3,4}
# s.add(5)
#2 .. remove () -> remove an element if the element didn't exists we will get an keyerror 
# s. remove (100)
# print(s)

# 3 . . discart () -> will not show any error if the 
# element is not present in set..
# s.discard (100)
# print(s)

# set operation..
# s1 = {1,2,3,4}
# s2 = {4,5,6,7,8}
# #1.. union ()
# merge both the sets
# print (f"union -> {s1.union (s2)}")

# 2 intersection 
# s1 = {1,2,3,4}
# s2 = {4,5,6,7,8}
# print (f"intersection -> {s1.intersection (s2)}")

#3 difference()
# s1 = {1,2,3,4}
# s2 = {4,5,,6,7,8}
# print (f" Difference -> {s1.difference (s2)}")
# print(f"Difference -> {s2.difference (s1)}")
#4 symmetric_ difference()
""""""
# s1 = {1,2,3,4}
# s2 = {4,5,6,7,8}
# print (f"Symmetric difference -> {s1.symetric_difference(s2)}")
#union (|) simbol 
#& -> intersection 
# - -> difference 
#^ -> symmetric difference 
  
# frozenset makes any set with  of fixed 
# element we cannot add element and we 
# cannot remove one.
# s = forozenset ([1,2,3,4,5,6])
# s.and (6)
# print(s)

# d ={10:100,2:200,3:300,4:400}
# d[10]=600
# print (d) # updating
 
# d = {10:100,2:200,3:300,4:400}
# d [50] = 500 #creating

