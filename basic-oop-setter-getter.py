''' Setter and Getter method
- Update value by passing to method
    + setter : set value to object (passing parameter)
    + getter : get value from object (return) '''

#%% Create class
class Employee:

    # Method Constructor
    def __init__(self, name, salary, department):
        # Set all attribute to private 
        self.__name =  name 
        self.__salary = salary 
        self.__department = department 

    # Method show data change to protected
    def _show_data(self):
        print(f"Employee name : {self.getName()}")
        print(f"Employee salary : {self.getSalary()}")
        print(f"Employee Department : {self.getDepartment()} ")
    
    # Setter name method
    def setName(self, new_name: str):
        self.__name = new_name
    
    # Setter salary method
    def setSalary(self, new_salary: int):
        self.__salary = new_salary

    # Setter department method
    def setDepartment(self, new_department: str):
        self.__department = new_department
    
    # Getter name method
    def getName(self) -> str:
        return self.__name
    
    # Getter salary method
    def getSalary(self) -> int:
        return self.__salary
    
    # Getter department method
    def getDepartment(self) -> str:
        return self.__department

# %% Create object
obj1 = Employee('Linda', 25000, 'Developer')

# Change value by call a method
obj1.setName('Loren')
obj1.setSalary(50000)
obj1.setDepartment('Manager')

# %% Call getter
print(f" name : {obj1.getName()} salary : {obj1.getSalary()} ")

# %% Show data
obj1._show_data()

# %%
