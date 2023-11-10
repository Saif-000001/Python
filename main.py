print("Hello World")

"""
Bangladesh is our country! ----> multi comment
"""

#if 5>2 : print('5 greater than 2') --->single comment 

"""
a = str(5)
b = float(6)
print(a)
print(b)

a = 'Salary'
A = 5
print(a)
print(A)
"""
#multiple variable
x, y, z = 'Saif', 5, 10
#print(x,y,type(z))

#one value multiple variable
x=y=z="Orange"
#print(x,y,z)

#Unpack a Collection
fruits = ['Apple', 'Banana', 'Cherry']
x, y, z = fruits
#print(type(fruits))
#print(x,y,z)

x = 'a'
y = 'b'
z = str(5)
#print(x+y+z)

#Global Variables
x='Awesome'

def myFun():
  global x 
  x= 'fantastic'
  #print('WoW '+x)
myFun()

#print("WoW "+x)
x = ("apple", "banana", "cherry")
#print(type(x))

x = {"name" : "John", "age" : 36}
#print(type(x))

x = 5
#print(complex(x)) (5+0j)