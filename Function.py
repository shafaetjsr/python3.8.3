def my_function():
    print('Hello from function')

my_function()

def my_function(vale):
    print('your value is : ' + vale)

my_function('shafaet')
my_function('age is 30')
my_function('12365478')

def my_fulname(fname,lnam):
    print('My Full name is : ' + fname +" "+lnam)

my_fulname('shafaet','hossain')

def my_val(*v):
    print('Your value is : '+v[2])

my_val('email','nummber','pass')


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")