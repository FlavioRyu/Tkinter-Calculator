# class tutorial

class Employee:
    
    num_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        
        Employee.num_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    

class Developer(Employee):
    raise_amt = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


emp1 = Employee('Flavio', 'Ryu', 1500)
emp2 = Employee('Giorgio', 'Moroder', 2000)

emp_str1 = 'Alberto-Digiulio-1700'
emp_str2 = 'Gianna-Falconi-1600'
emp_str3 = 'Maria-Lorenzini-1900'

new_emp1 = Employee.from_string(emp_str1)

print(new_emp1.email)
print(new_emp1.pay)

import datetime
my_date = datetime.date(2020, 6, 15)

print(Employee.is_workday(my_date))


dev1 = Developer('Gianni', 'Morandi', 780, 'Python')
dev2 = Developer('Gesù', 'Cristo', 0, 'Java')

print(dev1.prog_lang)
print(dev2.prog_lang)

