# Numeric, sequence type, Boolean, Set, Dictionary, Binary Types(memoryveiw, bytearray, bytes)


"""
# 01.Numeric -> integer, float, complex
a, b, c = 5, 7.5, 5j
print(type(a), type(b), type(c))
"""

"""
# 02.Sequence type -> string, tuple, list
# List[len(List)-3], it is enough to just write List[-3]. Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second-last item

a = "Hello World"
print(type(a))

tuple1 = ()
print("Initial empty tuple")
print(tuple1)

tuple2 = ('geeks', 'for', 'geeks')
print("Tuple with the use of string ")
print(tuple2)

tuple3 = (1,2,3,4)
print(tuple2, tuple3, sep='')

list = []
print("Initial empty list:")
print(list)

List = ["Geeks for Geeks"]
print(List)
List = ['a', 'b', 'c']
print(List)

List = [['a', 'b', 'c'], ['e', 'f', 'g']]
print(List)

list = ['Geeks', 'For', 'Geek']
print(list[2])
print(list[1])
print(list[0])
print(list[-1])
print(list[-3])
"""

"""
# 03.Boolean datatype -> True, False
print(type(True))
print(type(False))
# print(type(true)) -> Not allow
"""
"""
# 04.set data type 
set1 = set()
print('Initial empty set')
print(set1)

print('Set with the use of string')
set1 = set("geeksforgeeks")
print(set1)


set1 = set(['Geeks', 'for', 'Geeks'])
print(set1)

set1 = set([1,2,'Geeks', 4, 'For', 5])
print(set1)
"""

"""
# 05.Dictionary 
Dic = {}
print("Empty Dictionay: ")
print(Dic)

Dic = {1:"Geeks", 2:"For", 3:"Geek"}
print(Dic)

Dic = {'name':'geeks', 1:[1,2,3,4,5]}
print(Dic)

Dic = dict({1:'geeks', 2:'for', 3:'geek'})
print(Dic)

Dic = dict([(1, 'geeks'),(2, 'For')])
print(Dic)

print(Dic[1], Dic[2])
"""