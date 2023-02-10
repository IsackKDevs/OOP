#int this tutorial we will be using a class variable to raise a employess pay

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '' + last + '@google.come'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{}{}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        #i ould either use Employee.raise_amount or self.raise_amount

        
print(Employee.num_of_emps)
emp_1 = Employee("Isack", "kipanga", 5000)
emp1_raise = emp_1.apply_raise
print(emp1_raise)
