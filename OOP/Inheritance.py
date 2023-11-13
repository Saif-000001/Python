class Employee:

    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.email = fname+'.'+lname+'@company.com'
        self.pay = pay
        Employee.num_of_emp+=1

    def fullName(self):
        return '{}{}'.format(self.fname, self.lname)
    def apply_raise(self):
        self.pay = (self.pay*self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, fname, lname, pay, prg_language):
        super().__init__(fname, lname, pay)
        self.prg_language = prg_language

class Manager(Employee):
    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)
        if employees is None :
            self.employees = []
        else :
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self): 
        for emp in self.employees:
            print('--->', emp.fullName())      
    

# emp_1 = Developer('M','S',50000, 'python')
# emp_2 = Developer('S', 'I',60000, 'c++')

# mng_1 = Manager('S', 'K', 10000, [emp_1])
# print(emp_1.prg_language)
# print(emp_1.email)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)


emp_1 = Developer('M','S',50000, 'python')
emp_2 = Developer('S', 'I',60000, 'c++')

mng_1 = Manager('S', 'K', 10000, [emp_1])
# print(mng_1.email)
mng_1.add_emp(emp_2)
mng_1.remove_emp(emp_1)
mng_1.print_emps()


print(isinstance(mng_1, Manager))
print(isinstance(mng_1, Developer))
print(isinstance(mng_1, Employee))

print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))
