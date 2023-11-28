
# def fn(a, b):
#     return a + b
# add = fn(2, 5)
# print(add)

# building function
# a = abs(-5+2)
# print(a)

# ____________________String________________
# a = "hello world"
# b = "HELLO WORLD"
# x = a.upper()
# y = b.lower()
# print(x)
# print(y)

# a = "Bangladesh is beautiful"
# x = a.replace("beautiful", "Our Country")
# print(x)


# a = 'Hell! my students,Hell! my students,Hell! my students'
# x = a.split()
# print(x)

# print(a.find('my'))
# print(a.count('students'))

# a = "MSI"
# b = "SAIF"
# c = a + " "+b
# print(c)

# a = "Md. Saiful"
# b = "Islam"
# c = a + " "+ b
# print(c)

s = "banladesh is our country"

# print("".join(reversed(s)))
x = s.title()
print(x)

x = s.replace("banladesh", "is")
print(x)
list = x.split()
list.remove('is')
list.insert(1, "Banladesh")
s = ""
for i in list:
    s+=i+" "
print(s)
print(list)
print(x)