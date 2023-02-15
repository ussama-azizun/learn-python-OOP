''' Class and instance variable
  - Class : (global) does not need to create object can access
  - Instance : (local) require to create object  '''

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

# %% Create object
obj1 = Employee('Linda', 25000, 'Developer')
