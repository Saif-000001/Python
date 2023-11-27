# # Element of list in python
# v = ["Geeks", "For", "Geek"]
# print(v)

# # Creating a list in python
# # creat a list
# print("Blank List:")
# list = [] 
# print(list)

# # creat a list of number
# list = [5,6, 7]
# print("List of number:")
# print(list)

# list = [["Geeks", "For"], 
#         ["Geek"]
#         ]
# print(list[1][0])
# print(list[0][1])


# _______________Accessing___________________
# list = ["Firs",1,2,3,5, "Geeks", 7, "For", "Last"]
# print(list[-3])
# print(list[-1])
# print(list[0])

# print(list[-9])
# print(list[8])

# __________________Size of python list__________________
# list = ["Firs",1,2,3,5, "Geeks", 7, "For", "Last"]
# print(len(list))

# ____________________input of list______________________
# string = input("Input of the list : ")
# list = string.split()
# # list. reverse()
# # list.sort()
# print(list)

# ____________________________Adding Element_________________
# n = (int)(input())
# a = [int(i) for i in input().split()]
# print(a)

# using Append() method
# n = (int)(input())
# list = []

# for i in range(0, n):
#     list.append(i)

# print(list)

# list.append((2,5))
# print(list)

# list1 = ["Geeks", "For"]
# list.append(list1)
# print(list)

# using Insert() method
# list = [1,2,3,4,5]
# list.insert(1,25)
# list.insert(3,75)
# list.insert(0, "Geeks")
# print(list)

# using extend method
# list = [1,2,3,4]
# list1 = ["First", "Second"]
# list.extend(list1)
# print(list)

# _______________________Reverse list__________________
# list = ["geeks", 1,5,6,"ABC", 8,9]
# list.reverse()
# print(list)

# _____________________Remove list___________________
# list = [1,2,3,4,5,6,7,8,9]
# list.remove(2)

# for i in range(1, 5):
#     list.remove(i)
# list.pop()
# list.pop(2)
# print(list)


# list = [1, 2, 3, 4, 1, 1, 1, 4, 5] 
# print(list.index(1,1))


"""
list = [1,2,3,4,5,6]

for i in range(1, 5):
    list.remove(i)
print("Remove List: ", end="")
print(list)

for i in range(1,5):
    # list.append(i, i)
    list.insert(i-1,i)
print("Adding list: ", end="")
print(list)
"""