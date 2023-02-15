''' Class and instance variable
  - Class : (global) does not need to create object can access this variable
  - Instance : (local) require to create object  '''

#%% Create class
class Employee:

    # Class variable
    _min_salary = 12000
    _max_salary = 50000

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

# %% Create object
obj1 = Employee('Linda', 25000, 'Developer')

#%% Show data
obj1._show_data()
# %% Class variables
# Does not need to create an object for access class variable
print(f" Min salary {Employee._min_salary}")



# %%
