
# class
"""
class Employee:
    def __init__(self, fname, lname, pay):
       self.fname = fname
       self.lname = lname
       self.email = fname+'.'+lname+'@company.com'
       self.pay = pay


num_1 = Employee('M','S',50000)
num_2 = Employee('S','I',60000)
print(num_1.email)
print(num_2.email)
"""


# before class
"""
num_1 = Employee()
num_2 = Employee()
print(num_1)
print(num_2)

num_1.fname = "M"
num_1.lname = "S"
num_1.email = "M.S@company.com"
num_1.pay = 50000

num_2.fname = "S"
num_2.lname = "I"
num_2.email = "S.I@company.com"
num_2.pay = 60000
print(num_1.email)
print(num_2.email)
"""

# Method
"""
class Employee:
    def __init__(self, fname, lname, pay):
       self.fname = fname
       self.lname = lname
       self.email = fname+'.'+lname+'@company.com'
       self.pay = pay

    def fullName(self):
           return '{}{}'.format(self.fname, self.lname)
num_1 = Employee('M','S',50000)
num_2 = Employee('S','I',60000)

print(Employee.fullName(num_1))
print(Employee.fullName(num_2))

# print(num_1.fullName())
# print(num_2.fullName())
"""

# variables
"""
class Employee:
    nums_of_emps = 0
    raise_amount = 1.04
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.email = fname+'.'+lname+'@company.com'
        self.pay = pay

        Employee.nums_of_emps+=1

    def fullName(self):
        return '{}{}'.format(self.fname,self.lname)
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)

print(Employee.nums_of_emps)    
emp_1 = Employee('M','S',5000)
emp_2 = Employee('S','I',6000)
print(Employee.nums_of_emps)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
"""

# classMethod 
class Employee:
    num_of_emps = 0
    raise_amount = 1.04
     
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.email = fname+'.'+lname+'@company.com'
        self.pay = pay
        Employee.raise_amount+=1
    
    def fullName(self):
        return '{}{}'.format(self.fname,self.lname)
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    @classmethod
    def fromString(cls, empt_str):
        f, l, p = emp_str_1.split('-')
        return cls(f,l,p)
    @staticmethod
    def isWorkDay(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

emp_1 = Employee('M','S',50000)
emp_2 = Employee('S', 'I',60000)

# Employee.set_raise_amt(5)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

emp_str_1 = 'm-s-60000'
emp_str_2 = 's-i-50000'
emp_str_3 = 's-m-40000'

# f, l, p = emp_str_1.split('-')
# new_emp_1 = Employee(f,l,p)

# new_emp_1 = Employee.fromString(emp_str_1)
# print(new_emp_1.email)
# print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.isWorkDay(my_date))


