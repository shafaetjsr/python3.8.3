#print('hello world \n')


a = 'hello world'

#print(a)
#print(a[1])  # position  print and start with 0 index

print(a[2:5])

print(len(a)) # str length print

b = ' HELLO WORLD '
print(b.strip()) #  removes any whitespace from the beginning or the end

print(b.lower()) # string in lower case
print(a.upper()) # string in upper case
print(a.replace('h','z')) #  string replaces with another string

c = 'Hello , World'

print(c.split(',')) # string into substrings by separator ',

#d = 'rld' in c
d = 'rld' not in c
print(d) # phrase or character is present in a string

x = 'Hello'
y= 'World'
z = x + ' ' + y
print(z) # String Concatenation


name = 'Shafaet'
age = 30
country = 'Bangladesh'
AboutMe = "Hi, My Name is {} and My Age is {} and I live in {} and City is Dhaka."
AboutMebyindex = "Hi, My Name is {0} and My Age is {1} and I live in {2} and City is Dhaka."
print(AboutMe.format(name, age, country)) # use format() for query string
print(AboutMebyindex.format(name, age, country)) #use format() for query string by Index

p = 'I am shafaet and Live in \"Dhaka\" city'
print(p)
