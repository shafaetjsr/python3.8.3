# If statements

a = 33
b = 33
if b>a:
 print('b is greater then a')
elif a==b:
    print('a and b are equal')
else:
    print('a is greater then b')

# While Loop

i = 1
while i < 6:
  print(i)
  i += 1


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# For Loop

fruits = ["apple", "banana", "cherry"]

for x in fruits:
  print(x)

for x in range(2, 30, 3):
  print(x)

for x in range(6):
  print(x)