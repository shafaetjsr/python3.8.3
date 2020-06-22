# There are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

fruitList = ['apple','banana','cherry']
print(fruitList) #print all value

print(fruitList[1]) # print index value ='banana'

print(fruitList[-1]) # print last value

fruitList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruitList[2:5]) # between value

print(fruitList[:4]) # first 4 item

print(fruitList[2:]) # after 2 item

fruitList[1]='lemon'
print(fruitList) # replace index

for x in fruitList: # assaign valu in x
    print(x)

print(len(x)) # check length

#Tuple

# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

# set
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

thisset = {"apple", "banana", "cherry"}
print(thisset)