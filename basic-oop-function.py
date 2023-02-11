''' Functions 
 - isisstance : check whether object was create from class
 - dir : show attr and method
 - __class__ : show class name of object '''

#%% Create class
class Employee:

    # Method Constructor
    def __init__(self, name, salary, department):
        self.name =  name # name
        self.salary = salary #salary
        self.department = department #department

    # Method show data
    def show_data(self):
        print(f"Employee name {self.name}")
        print(f"Employee salary {self.salary}")
        print(f"Employee Department {self.department} ")

#%% Create object
obj1 = Employee('Linda', 25000, 'Developer')
obj2 = Employee('Loren', 50000, 'Manager')

# %% Check was obj1  created from Employee class?
print(isinstance(obj1, Employee))

# %% Check obj1 method and attribute
print(dir(obj1.show_data))

# %% Check 
print(obj1.__class__)

# %%
