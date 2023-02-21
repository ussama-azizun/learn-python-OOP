'''
Polymorphism
 - Overloading method : which method in the same class and name, but different parameter (Polymorphism)
 - Overriding method : method of subclass which have same name with superclass (inheritance)
'''

#%% Overloading
class Employee:

    # Class variable
    min_salary = 12000
    max_salary = 50000
    company_name = "WY Corporation"

    # Method Constructor
    def __init__(self, name, salary, department):
        # Instance variable
        self.__name =  name 
        self.__salary = salary 
        self._department = department 

    # Method show data change to protected
    def _show_data(self):
        print(f"Employee name : {self.__name}")
        print(f"Employee salary : {self.__salary}")
        print(f"Employee Department : {self._department} ")
    
    def _yearly_salary(self):
        return self.__salary * 12
    
    def __str__(self) -> str:
        return (f"Employee name : {self.__name}, Salary : {self.__salary}, yearly : {self._yearly_salary()}")

#%% Create  Subclass
class Accounting(Employee):
    __department_name = 'Accounting'

    def __init__(self, name, salary):
        super().__init__(name, salary, self.__department_name)
    

class Programmer(Employee):
    __department_name = 'Developer'

    def __init__(self, name, salary):
        super().__init__(name, salary, self.__department_name)
        # super()._show_data() # Call by Superclass

class Sale(Employee):
    __department_name = 'Sale'

    def __init__(self, name, salary):
        super().__init__(name, salary, self.__department_name)

