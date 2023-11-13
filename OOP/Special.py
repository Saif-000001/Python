"""
class Employee:
    raise_amount = 1.04
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.email = fname+'.'+lname+'@gmail.com'
        self.pay = pay
    
    def fullName(self):
        return '{}{}'.format(self.fname, self.lname)
    def apply_raise(self):
        self.pay = (self.pay*Employee.raise_amount)
    
    def __repr__(self):
        return "Employee('{}','{}', '{}')".format(self.fname, self.lname, self.pay)
    def __str__(self):
        return '{} - {}'.format(self.fullName(), self.email)
        
    
emp_1 = Employee('S', 'K', 50000)
emp_2 = Employee('M','S',60000)

# print(emp_1)

# print(repr(emp_1))
# print(repr(emp_2))

print(str(emp_1))
print(str(emp_2))

print(emp_1.__repr__())
print(emp_1.__str__())
"""

# Property Decorators - Getters, Setters, and Deleters
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.fname, self.lname)
    @property
    def fullName(self):
        return '{} {}'.format(self.fname, self.lname)
    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ')
        self.fname = first
        self.lname = last

emp1 = Employee('M','S')

# print(emp1.email())
# print(emp1.fullName())

# print(emp1.email)
# print(emp1.fullName)

emp1.fullName = 'MSI SAIF'
print(emp1.fullName)


