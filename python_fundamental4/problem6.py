from abc import ABC ,abstractmethod
class Employee:
    def calculate_salary(self):
        pass
class Intern(Employee):
    def calculate_salary(self,salary):
        self.salary=salary
        print(f"Salary of intern is {self.salary}")
class FullTimeEmployee(Employee):
    def calculate_salary(self,salary):
        self.salary=salary
        print(f"Salary of Fulltime employee is {self.salary}")
class ContractEmployee(Employee):
    def calculate_salary(self,salary):
        self.salary=salary
        print(f"Salary of Contract Employee is {self.salary}")

sal=ContractEmployee()
sal.calculate_salary(50_00_000)