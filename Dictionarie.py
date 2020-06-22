carDis = {
    'brand' :'Ford',
    'model' : 'Mustang',
    'year' : 1964
}

print(carDis)

# x = carDis['model']
x =carDis.get('model')
print(x)

carDis['year']=2018
print(carDis)

for y in carDis:
    print(y)

for a in carDis:
    print(carDis[a])


for m,n in carDis.items():
    print(m,'=> ',n)


print(len(carDis))

carDis['color'] ='red'
print(carDis)

#carDis.pop('model')

#carDis.popitem()

#print(carDis)

#carDis.clear()
#print(carDis)

myCare = carDis.copy()
print( myCare)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 

for v in myfamily:
    print(myfamily[v])