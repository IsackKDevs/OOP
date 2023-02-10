

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '' + last + '@google.come'

    def fullname(self):
        return '{}{}'.format(self.first,self.last)

        

emp_1 = Employee("Isack", "kipanga", 5000)
print(emp_1.fullname())